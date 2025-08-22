#!/usr/bin/env python3

###
# Generates build files for the project.
# This file also includes the project configuration,
# such as compiler flags and the object matching status.
#
# Usage:
#   python3 configure.py
#   ninja
#
# Append --help to see available options.
###

import argparse
import sys
from pathlib import Path
from typing import Any, Dict, List

from tools.project import (
    Object,
    ProgressCategory,
    ProjectConfig,
    calculate_progress,
    generate_build,
    is_windows,
)

# Game versions
DEFAULT_VERSION = 0
VERSIONS = [
    "GKYE",  # 0
]

parser = argparse.ArgumentParser()
parser.add_argument(
    "mode",
    choices=["configure", "progress"],
    default="configure",
    help="script mode (default: configure)",
    nargs="?",
)
parser.add_argument(
    "-v",
    "--version",
    choices=VERSIONS,
    type=str.upper,
    default=VERSIONS[DEFAULT_VERSION],
    help="version to build",
)
parser.add_argument(
    "--build-dir",
    metavar="DIR",
    type=Path,
    default=Path("build"),
    help="base build directory (default: build)",
)
parser.add_argument(
    "--binutils",
    metavar="BINARY",
    type=Path,
    help="path to binutils (optional)",
)
parser.add_argument(
    "--compilers",
    metavar="DIR",
    type=Path,
    help="path to compilers (optional)",
)
parser.add_argument(
    "--map",
    action="store_true",
    help="generate map file(s)",
)
parser.add_argument(
    "--debug",
    action="store_true",
    help="build with debug info (non-matching)",
)
if not is_windows():
    parser.add_argument(
        "--wrapper",
        metavar="BINARY",
        type=Path,
        help="path to wibo or wine (optional)",
    )
parser.add_argument(
    "--dtk",
    metavar="BINARY | DIR",
    type=Path,
    help="path to decomp-toolkit binary or source (optional)",
)
parser.add_argument(
    "--objdiff",
    metavar="BINARY | DIR",
    type=Path,
    help="path to objdiff-cli binary or source (optional)",
)
parser.add_argument(
    "--sjiswrap",
    metavar="EXE",
    type=Path,
    help="path to sjiswrap.exe (optional)",
)
parser.add_argument(
    "--ninja",
    metavar="BINARY",
    type=Path,
    help="path to ninja binary (optional)"
)
parser.add_argument(
    "--verbose",
    action="store_true",
    help="print verbose output",
)
parser.add_argument(
    "--non-matching",
    dest="non_matching",
    action="store_true",
    help="builds equivalent (but non-matching) or modded objects",
)
parser.add_argument(
    "--warn",
    dest="warn",
    type=str,
    choices=["all", "off", "error"],
    help="how to handle warnings",
)
parser.add_argument(
    "--no-progress",
    dest="progress",
    action="store_false",
    help="disable progress calculation",
)
args = parser.parse_args()

config = ProjectConfig()
config.version = str(args.version)
version_num = VERSIONS.index(config.version)

# Apply arguments
config.build_dir = args.build_dir
config.dtk_path = args.dtk
config.objdiff_path = args.objdiff
config.binutils_path = args.binutils
config.compilers_path = args.compilers
config.generate_map = args.map
config.non_matching = args.non_matching
config.sjiswrap_path = args.sjiswrap
config.ninja_path = args.ninja
config.progress = args.progress
if not is_windows():
    config.wrapper = args.wrapper
# Don't build asm unless we're --non-matching
if not config.non_matching:
    config.asm_dir = None

# Tool versions
config.binutils_tag = "2.42-1"
config.compilers_tag = "20250812"
config.dtk_tag = "v1.6.2"
config.objdiff_tag = "v3.0.0-beta.14"
config.sjiswrap_tag = "v1.2.1"
config.wibo_tag = "0.7.0"

# Project
config.config_path = Path("config") / config.version / "config.yml"
config.check_sha_path = Path("config") / config.version / "build.sha1"
config.asflags = [
    "-mgekko",
    "--strip-local-absolute",
    "-I include",
    f"-I build/{config.version}/include",
    f"--defsym BUILD_VERSION={version_num}",
]
config.ldflags = [
    "-fp hardware",
    "-nodefaults",
]
if args.debug:
    config.ldflags.append("-g")  # Or -gdwarf-2 for Wii linkers
if args.map:
    config.ldflags.append("-mapunused")
    # config.ldflags.append("-listclosure") # For Wii linkers

# Use for any additional files that should cause a re-configure when modified
config.reconfig_deps = []

# Optional numeric ID for decomp.me preset
# Can be overridden in libraries or objects
config.scratch_preset_id = None

# Base flags, common to most GC/Wii games.
# Generally leave untouched, with overrides added below.
cflags_base = [
    "-nodefaults",
    "-proc gekko",
    "-align powerpc",
    "-enum int",
    "-fp hardware",
    "-Cpp_exceptions off",
    # "-W all",
    "-O4,p",
    "-inline auto",
    '-pragma "cats off"',
    '-pragma "warn_notinlined off"',
    "-maxerrors 1",
    "-nosyspath",
    "-RTTI off",
    "-fp_contract on",
    "-str reuse",
    "-multibyte",  # For Wii compilers, replace with `-enc SJIS`
    "-i include",
    f"-i build/{config.version}/include",
    f"-DBUILD_VERSION={version_num}",
    f"-DVERSION_{config.version}",
]

# Debug flags
if args.debug:
    # Or -sym dwarf-2 for Wii compilers
    cflags_base.extend(["-sym on", "-DDEBUG=1"])
else:
    cflags_base.append("-DNDEBUG=1")

# Warning flags
if args.warn == "all":
    cflags_base.append("-W all")
elif args.warn == "off":
    cflags_base.append("-W off")
elif args.warn == "error":
    cflags_base.append("-W error")

# Metrowerks library flags
cflags_runtime = [
    *cflags_base,
    "-use_lmw_stmw on",
    "-str reuse,pool,readonly",
    "-gccinc",
    "-common off",
    "-inline auto",
]

# REL flags
cflags_rel = [
    *cflags_base,
    "-sdata 0",
    "-sdata2 0",
]

config.linker_version = "GC/1.3.2"


# Helper function for Dolphin libraries
def DolphinLib(lib_name: str, objects: List[Object]) -> Dict[str, Any]:
    return {
        "lib": lib_name,
        "mw_version": "GC/1.2.5n",
        "cflags": cflags_base,
        "progress_category": "sdk",
        "objects": objects,
    }


# Helper function for REL script objects
def Rel(lib_name: str, objects: List[Object]) -> Dict[str, Any]:
    return {
        "lib": lib_name,
        "mw_version": "GC/1.3.2",
        "cflags": cflags_rel,
        "progress_category": "game",
        "objects": objects,
    }


Matching = True                   # Object matches and should be linked
NonMatching = False               # Object does not match and should not be linked
Equivalent = config.non_matching  # Object should be linked when configured with --non-matching


# Object is only matching for specific versions
def MatchingFor(*versions):
    return config.version in versions


config.warn_missing_config = True
config.warn_missing_source = False
config.libs = [
    {
        "lib": "Runtime.PPCEABI.H",
        "mw_version": config.linker_version,
        "cflags": cflags_runtime,
        "progress_category": "sdk",  # str | List[str]
        "objects": [
            Object(NonMatching, "Runtime.PPCEABI.H/global_destructor_chain.c"),
            Object(NonMatching, "Runtime.PPCEABI.H/__init_cpp_exceptions.cpp"),
        ],
    },
    {
        "lib": "GameCode",
        "mw_version": config.linker_version,
        "cflags": cflags_rel,
        "progress_category": "game",
        "objects": [
            # Game Mode Objects
            Object(NonMatching, "gmmain.o"),
            Object(NonMatching, "gmglobal.o"),
            Object(NonMatching, "gmautodemo.o"),
            Object(NonMatching, "gmracecommon.o"),
            Object(NonMatching, "gmracenormal.o"),
            Object(NonMatching, "gmdialogue.o"),
            Object(NonMatching, "gmdialoguesub.o"),
            Object(NonMatching, "gmdialoguestatus.o"),
            Object(NonMatching, "gmspecialmovie.o"),
            Object(NonMatching, "gmclearchecker.o"),
            Object(NonMatching, "gmviconfigure.o"),
            Object(NonMatching, "gmlanmenu.o"),
            
            # Library Objects
            Object(NonMatching, "lbairride.o"),
            
            # Air Ride C++ Objects
            Object(NonMatching, "a2d_game_lib.o"),
            Object(NonMatching, "a2d_gamehistory.o"),
            Object(NonMatching, "a2d_gamesession.o"),
            Object(NonMatching, "a2d_cpu_kirby.o"),
            Object(NonMatching, "a2d_kirbyjointanim.o"),
            Object(NonMatching, "a2d_lavabomb.o"),
            Object(NonMatching, "a2d_grindrail.o"),
            Object(NonMatching, "a2d_bg3000.o"),
            Object(NonMatching, "a2d_bg4000.o"),
            Object(NonMatching, "a2d_bg5000.o"),
            Object(NonMatching, "a2d_bg8000.o"),
            Object(NonMatching, "a2d_kurakko.o"),
            Object(NonMatching, "a2d_game_audio.o"),
            Object(NonMatching, "a2d_soundhandle.o"),
            Object(NonMatching, "a2d_game_effect.o"),
            Object(NonMatching, "a2d_effecthandle.o"),
            Object(NonMatching, "a2d_wipeeffect.o"),
            Object(NonMatching, "a2d_effect_slideblur.o"),
            Object(NonMatching, "a2d_kirbydisp.o"),
            Object(NonMatching, "a2d_refract.o"),
            
            # Graphics Objects
            Object(NonMatching, "grcity1.o"),
            
            # Text/Data Objects
            Object(NonMatching, "text_80060ED0.o"),
            Object(NonMatching, "db_800AD79C.o"),
            Object(NonMatching, "smsoundtest.o"),
            Object(NonMatching, "text_800AF474.o"),
            Object(NonMatching, "text_8010F854.o"),
            Object(NonMatching, "text_801166B4.o"),
            Object(NonMatching, "text_801D443C.o"),
            Object(NonMatching, "text_8028B974.o"),
            Object(NonMatching, "text_8034D384.o"),
            Object(NonMatching, "text_803AFAC8.o"),
            Object(NonMatching, "text_8042AD44.o"),
            Object(NonMatching, "text_8045DAE4.o"),
            Object(NonMatching, "text_8047DB6C.o"),
            Object(NonMatching, "text_80482598.o"),
        ],
    },
    {
        "lib": "DolphinSDK",
        "mw_version": "GC/1.2.5n",
        "cflags": cflags_base,
        "progress_category": "sdk",
        "objects": [
            # Dolphin SDK Objects
            Object(NonMatching, "dolphin_sdk_other.o"),
            Object(NonMatching, "dolphin_sdk_db.o"),
            Object(NonMatching, "dolphin_sdk_dsp.o"),
            Object(NonMatching, "dolphin_sdk_dvd.o"),
            Object(NonMatching, "dolphin_sdk_gx.o"),
            Object(NonMatching, "dolphin_sdk_mtx.o"),
            Object(NonMatching, "dolphin_sdk_mtxvec.o"),
            Object(NonMatching, "dolphin_sdk_mtx44.o"),
            Object(NonMatching, "dolphin_sdk_vec.o"),
            Object(NonMatching, "dolphin_sdk_os.o"),
            Object(NonMatching, "dolphin_sdk_pad.o"),
            Object(NonMatching, "dolphin_sdk_vi.o"),
            Object(NonMatching, "dolphin_sdk_ai.o"),
            Object(NonMatching, "dolphin_sdk_ar.o"),
            Object(NonMatching, "dolphin_sdk_arq.o"),
            Object(NonMatching, "dolphin_sdk_card.o"),
            Object(NonMatching, "dolphin_sdk_si.o"),
            Object(NonMatching, "dolphin_sdk_exi.o"),
            Object(NonMatching, "dolphin_sdk_ax.o"),
            Object(NonMatching, "dolphin_sdk_mix.o"),
            Object(NonMatching, "dolphin_sdk_synth.o"),
            Object(NonMatching, "dolphin_data.o"),
            Object(NonMatching, "dobj.o"),
            Object(NonMatching, "tobj.o"),
            Object(NonMatching, "tev.o"),
            Object(NonMatching, "mobj.o"),
            Object(NonMatching, "aobj.o"),
            Object(NonMatching, "lobj.o"),
            Object(NonMatching, "cobj.o"),
            Object(NonMatching, "fobj.o"),
            Object(NonMatching, "pobj.o"),
            Object(NonMatching, "jobj.o"),
            Object(NonMatching, "displayfunc.o"),
            Object(NonMatching, "initialize.o"),
            Object(NonMatching, "video.o"),
            Object(NonMatching, "controller.o"),
            Object(NonMatching, "rumble.o"),
            Object(NonMatching, "spline.o"),
            Object(NonMatching, "mtx.o"),
            Object(NonMatching, "util.o"),
            Object(NonMatching, "objalloc.o"),
            Object(NonMatching, "robj.o"),
            Object(NonMatching, "id.o"),
            Object(NonMatching, "wobj.o"),
            Object(NonMatching, "fog.o"),
            Object(NonMatching, "pref.o"),
            Object(NonMatching, "list.o"),
            Object(NonMatching, "object.o"),
            Object(NonMatching, "memory.o"),
            Object(NonMatching, "shadow.o"),
            Object(NonMatching, "archive.o"),
            Object(NonMatching, "random.o"),
            Object(NonMatching, "bytecode.o"),
            Object(NonMatching, "class.o"),
            Object(NonMatching, "hash.o"),
            Object(NonMatching, "texp.o"),
            Object(NonMatching, "texpdag.o"),
            Object(NonMatching, "debug.o"),
            Object(NonMatching, "gobjproc.o"),
            Object(NonMatching, "gobjplink.o"),
            Object(NonMatching, "gobjgxlink.o"),
            Object(NonMatching, "gobjobject.o"),
            Object(NonMatching, "gobjuserdata.o"),
            Object(NonMatching, "gobj.o"),
            Object(NonMatching, "particle.o"),
            Object(NonMatching, "axdriver.o"),
            Object(NonMatching, "HVQM4Bufv.o"),
            Object(NonMatching, "IPSocket.o"),
            Object(NonMatching, "IPIgmp.o"),
            
            # Additional objects
            Object(NonMatching, "fl_indirectload.o"),
            Object(NonMatching, "__va_arg.o"),
            Object(NonMatching, "global_destructor_chain.o"),
            Object(NonMatching, "NMWException.o"),
            Object(NonMatching, "MWRTTI.o"),
            Object(NonMatching, "runtime.o"),
            Object(NonMatching, "Gecko_ExceptionPPC.o"),
            Object(NonMatching, "GCN_mem_alloc.o"),
            Object(NonMatching, "abort_exit.o"),
            Object(NonMatching, "cstring.o"),
            Object(NonMatching, "TRK_MINNOW_DOLPHIN.o"),
            Object(NonMatching, "PPCArch.o"),
            Object(NonMatching, "__mem.o"),
            Object(NonMatching, "mem_TRK.o"),
            Object(NonMatching, "__exception.o"),
            Object(NonMatching, "__start.o"),
            Object(NonMatching, "__ppc_eabi_init.o"),
        ],
    },
]


# Optional callback to adjust link order. This can be used to add, remove, or reorder objects.
# This is called once per module, with the module ID and the current link order.
#
# For example, this adds "dummy.c" to the end of the DOL link order if configured with --non-matching.
# "dummy.c" *must* be configured as a Matching (or Equivalent) object in order to be linked.
def link_order_callback(module_id: int, objects: List[str]) -> List[str]:
    # Don't modify the link order for matching builds
    if not config.non_matching:
        return objects
    if module_id == 0:  # DOL
        return objects + ["dummy.c"]
    return objects

# Uncomment to enable the link order callback.
# config.link_order_callback = link_order_callback


# Optional extra categories for progress tracking
# Adjust as desired for your project
config.progress_categories = [
    ProgressCategory("game", "Game Code"),
    ProgressCategory("sdk", "SDK Code"),
]
config.progress_each_module = args.verbose
# Optional extra arguments to `objdiff-cli report generate`
config.progress_report_args = [
    # Marks relocations as mismatching if the target value is different
    # Default is "functionRelocDiffs=none", which is most lenient
    # "--config functionRelocDiffs=data_value",
]

if args.mode == "configure":
    # Write build.ninja and objdiff.json
    generate_build(config)
elif args.mode == "progress":
    # Print progress information
    calculate_progress(config)
else:
    sys.exit("Unknown mode: " + args.mode)

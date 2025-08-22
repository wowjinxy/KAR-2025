# Assert String Analysis

This document maps assert strings found in the binary to their source functions and files, helping identify function purposes and locations.

## Assert String Locations and Functions

### Game Object (GObj) Related Asserts

#### `HSD_GObjGetId(gobj) == Gm_GObj_Id_Airflow`
- **Address**: `0x8049f040`
- **File**: `dbmapgravity.c`
- **Functions**: 
  - `FUN_800a7994` @ `0x800a7994` (line 0x374 = 884)
  - `FUN_800a7a34` @ `0x800a7a34`
- **Purpose**: Validates airflow game objects in map gravity system

#### `no such player%d gobj!`
- **Address**: `0x804a214c` 
- **File**: `cmlib.c` (camera library)
- **Functions**:
  - `FUN_800ba7b4` @ `0x800ba7b4` (line 0x3e5 = 997)
  - `FUN_800b9c74` @ `0x800b9c74`
- **Purpose**: Player game object validation in camera system

#### `gyp->lc.cannon.userInfo[i].gobj`
- **Address**: `0x804a6474`
- **File**: `gryakucannon.c`
- **Functions**:
  - `FUN_800fee40` @ `0x800fee40`
  - `FUN_800ff010` @ `0x800ff010`
- **Purpose**: Validates cannon user info game objects

### Source File Name Strings

These strings indicate original source file names and help map functions to their object files:

#### Game Mode Files
- `gmmain.c` @ `0x80494e88`
- `gmglobal.c` @ `0x80495010`
- `gmautodemo.c` @ `0x80495c14`
- `gmracecommon.c` @ `0x8049615c`
- `gmracenormal.c` @ `0x80496178`
- `gmdialogue.c` @ `0x80496f38`
- `gmdialoguesub.c` @ `0x80497280`
- `gmdialoguestatus.c` @ `0x804972d8`
- `gmspecialmovie.c` @ `0x804972f0`
- `gmclearchecker.c` @ `0x80497584`
- `gmviconfigure.c` @ `0x80497ba5`
- `gmlanmenu.c` @ `0x80497bb8`

#### Library Files (lb*)
- `lbairride.c` @ `0x80497d74`
- `lblight.c` @ `0x80497e00`
- `lbmemory.c` @ `0x80497e10`
- `lbheap.c` @ `0x80497f60`
- `lbfile.c` @ `0x80498108`
- `lbarchive.c` @ `0x804981a4`
- `lbaudio.c` @ `0x80498fc4`
- `lbvector.c` @ `0x804994b8` (with assert marker `!`)
- `lbfade.c` @ `0x804994b8`
- `lbcamera.c` @ `0x80499618`
- `lbcolanim.c` @ `0x80499808`
- `lbspline.c` @ `0x80499840`
- `lbkdtree.c` @ `0x80499860`
- `lbkdcoll.c` @ `0x80499ccc`
- `lbhvqm.c` @ `0x8049aa28`
- `lbarealight.c` @ `0x8049acac`
- `lbarealightuser.c` @ `0x8049ad54`
- `lbarealightzone.c` @ `0x8049ad98`
- `lbshadow.c` @ `0x8049add4`

#### Debug Files (db*)
- `dbposition.c` @ `0x8049bf18`
- `dbscreenshot.c` @ `0x8049bfb0`
- `dbcamera.c` @ `0x8049d7fb`
- `dbmapspline.c` @ `0x8049e768`
- `dbmapzone.c` @ `0x8049ed90`
- `dbmapmpcoll.c` @ `0x8049ede0`
- `dbmapdispbbox.c` @ `0x8049ee93` (with assert marker `!`)
- `dbmapgravity.c` @ `0x8049ef90`

#### Ground/Map Files (gr*)
- `ground.c` @ `0x804a23e8`
- `grdata.c` @ `0x804a32d0`
- `grlib2.c` @ `0x804a3b40`
- `grcoll.c` @ `0x804a3bbc`
- `grparts.c` @ `0x804a3e10`
- `grcommon.c` @ `0x804a3eac`
- `granim.c` @ `0x804a3ee0`
- `grrough.c` @ `0x804a3f38`
- `grzone.c` @ `0x804a4098`
- `grzonecover.c` @ `0x804a4170`
- `grkdtree.c` @ `0x804a4180`
- `grcoursespline.c` @ `0x804a4210`
- `grrangespline.c` @ `0x804a4530`
- `grnullpos.c` @ `0x804a4820`
- `grdispbbox.c` @ `0x804a4a00`
- `grgravity.c` @ `0x804a4a60`
- `grairflow.c` @ `0x804a4a80`
- `grconveyer.c` @ `0x804a4bc0`
- `grswitch.c` @ `0x804a4ee0`
- `grrail.c` @ `0x804a5040`
- `graudio.c` @ `0x804a50c8`
- `grboxgenerator.c` @ `0x804a51f8`
- `greventgenerator.c` @ `0x804a5550`
- `grglobaldead.c` @ `0x804a5618`
- `grpointstrike.c` @ `0x804a5648`
- `grairglider.c` @ `0x804a56f0`

#### Camera Files (cm*)
- `camera.c` @ `0x804a207c`
- `cmreplay.c` @ `0x804a227c`
- `cmanimation.c` @ `0x804a23c8`

#### Sound Files
- `textlib.c` @ `0x8049f388`
- `lsmsoundtest.c` @ `0x804a128b`

#### Yaku Files (gryaku*)
- `gryaku.c` @ `0x804a5824`
- `gryakuanim.c` @ `0x804a5ac0`
- `gryakueffect.c` @ `0x804a5ae8`
- `gryakuaudio.c` @ `0x804a5b30`
- `gryakulib.c` @ `0x804a5b60`
- `gryakucommon.c` @ `0x804a5d40`
- `gryakudownforcezone.c` @ `0x804a5efc`
- `gryakucatchzone.c` @ `0x804a5f64`
- `gryakurecoveryzone.c` @ `0x804a6044`
- `gryakurotjumphill.c` @ `0x804a617c`
- `gryakuinvisibleball.c` @ `0x804a6234`
- `gryakurisingcube.c` @ `0x804a62e7`
- `gryakugondola.c` @ `0x804a63d0`
- `gryakucannon.c` @ `0x804a6464`
- `gryakupushoutwall.c` @ `0x804a6510`
- `gryakulighttunnel.c` @ `0x804a662c`
- `gryakupillar.c` @ `0x804a66b8`
- `gryakubreakrock.c` @ `0x804a685c`
- `gryakubreakhouse.c` @ `0x804a68fc`
- `gryakuanimfloor.c` @ `0x804a69e4`
- `gryakubreakcoral.c` @ `0x804a6a9c`
- `gryakubreakicicle.c` @ `0x804a6ba4`
- `gryakubreakcommon.c` @ `0x804a6bf0`
- `gryakulasergate.c` @ `0x804a6d10`
- `gryakubreakfloor.c` @ `0x804a6e1c`

### SDK Assert Strings

#### Memory Management Asserts
- `GCN_Mem_Alloc.c : InitDefaultHeap. No Heap Available` @ `0x8048b6b8`

#### OS Thread/Heap Checking Asserts
Multiple detailed OS checking asserts from `0x804fa5e8` to `0x804fc448` covering:
- Heap validation (`OSCheckHeap`)
- Thread management (`OSCheckActiveThreads`)
- Memory alignment checks
- Queue validation

#### TRK Debug System Asserts
Multiple TRK (MetroTRK debugging) messages from `0x8048bc00` onwards.

### Specific Assert Conditions Found

#### Game Object Validation
- `HSD_GObjGetId(gobj) == Gm_GObj_Id_Airflow`
- `grYakuGetKind(yakuGObj) == Gr_YakuKind_Cannon`
- `grYakuGetKind(gobj) == Gr_YakuKind_RecoveryZone`
- `grYakuChkClassicalScaling(gobj)`
- `grYakuCheckGObjYakumono(yakuGObj)`
- `vcGObj != NULL`
- `lighthouseGObj`

#### Parameter Validation
- `param->upTargetNum <= GrYakuRisingCubeCtrl_GObjNumMax`
- `param->downTargetNum <= GrYakuRisingCubeCtrl_GObjNumMax`
- `0 < param->targetNum && param->targetNum <= GrYakuPushOutWallCtrl_GObjNumMax`
- `0 < param->endTargetNum && param->endTargetNum <= GrYakuPushOutWallCtrl_GObjNumMax`
- `param->targetNum <= GrYakuPillarCtrl_GObjNumMax`
- `0 < param->targetNum && param->targetNum <= GrYakuLaserGateCtrl_GObjNumMax`

#### Memory/Pointer Validation
- `gyp->lc.gondola.userGObj`
- `gyp->lc.gondola.userGObj == oldAppGObj`
- `gyp->lc.cannon.userInfo[i].gobj`
- `bestrapbg_gobj is NULL!`

### KDTree Assert
- `lbKdObjCreateFunc[type].chkIncludeNodeFuncOne(&kdtree->node[0]->box, data)` @ `0x80499b54`

### Break Floor Assert
- `gyp->lc.breakFloor.currentAnim >= 1 && gyp->lc.breakFloor.currentAnim <= param->wpp->crackStateNum` @ `0x804a6e40`

## Analysis Summary

The assert strings reveal:

1. **File Organization**: Clear separation between game modes (gm*), libraries (lb*), ground/map (gr*), debug (db*), camera (cm*), and yaku (gryaku*) systems.

2. **Function Purposes**: Many functions are game object validators, parameter checkers, and system initializers.

3. **Memory Layout**: The addresses show that assert strings are stored in the `.rodata` section, providing a map of where different object files are located.

4. **Assert Patterns**: Most asserts follow standard patterns:
   - NULL pointer checks
   - Bounds checking
   - Game object ID validation
   - Parameter validation

5. **Development Practices**: The presence of assert strings with source file names and line numbers indicates this was a debug build or the asserts were not stripped.

## Next Steps

Use these assert string locations to:
1. Map functions to their correct source files
2. Identify function purposes based on assert conditions
3. Locate boundaries between object files
4. Rename functions with meaningful names based on their assert context


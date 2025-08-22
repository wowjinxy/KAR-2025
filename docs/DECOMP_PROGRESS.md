# Kirby Air Ride Decompilation Progress

## Project Overview
This is a decompilation project for Kirby Air Ride (GKYE) using DTK (Decomp Toolkit).

## Build Information
- **Target**: Kirby Air Ride (GameCube, NTSC-U)
- **Game ID**: GKYE
- **Compiler**: Metrowerks CodeWarrior 2.4.2 build 81 (GC MW 1.3.2)
- **Compiler Flags**: `-O4,p -nodefaults -fp hard -Cpp_exceptions off -enum int -fp_contract on -inline auto`
- **Total Objects**: 145 split objects
  - **Game Code**: 48 files (0.00% matched)
  - **SDK Code**: 86 files (0.00% matched)

## Current Status
- ✅ **DTK Setup Complete** - Build system working, all objects split
- ✅ **gmmain.o Analysis Complete** - All 8 functions identified and named
- ✅ **gmglobal.o Analysis Complete** - All functions identified, transition point found
- ⏳ **gmautodemo.o Analysis Pending** - Ready to begin analysis
- ⏳ **Remaining Objects** - 142 objects pending analysis

## Memory Layout
- **SDK/Library Functions**: `0x80380000-0x803BFFFF`
- **MetroTRK Functions**: `0x803C0000-0x803DFFFF`
- **Game Code**: Starting around `0x80005800`

## Key Files
- `KAR-2025/config/GKYE/config.yml` - DTK configuration
- `KAR-2025/config/GKYE/symbols.txt` - Function and data symbols
- `KAR-2025/config/GKYE/splits.txt` - Memory section definitions
- `KAR-2025/configure.py` - Build system configuration
- `KAR-2025/config/GKYE/build.sha1` - Expected output checksum

## Build Commands
```bash
cd KAR-2025
ninja  # Build and verify
```

## Notes
- The game has sophisticated debug modes (gDebugLevel: 0, 1, 3+)
- E3 build flag support (gE3BuildFlag)
- Memory management optimizations for different console configurations
- Auto-demo system for title screen idle timeout

## Top Ride (a2d) System
- **Separate C++ Implementation** - Independent from main C-based game
- **Comprehensive Racing System** - 20+ C++ source files identified
- **Independent Data Management** - Separate file structure with "A2" prefix
- **Advanced Features** - AI, effects, audio, and multiple track systems
- **Documentation**: See `TOP_RIDE_ANALYSIS.md` for complete analysis

## Game Manager (gm) Systems
- **Core Game Architecture** - 15+ identified gm systems
- **Comprehensive Management** - Mode, scene, racing, dialogue, and media systems
- **Advanced Audio Management** - FGM and BGM systems with extensive controls
- **Robust Error Handling** - Comprehensive validation and debugging features
- **Documentation**: See `GAME_MANAGER_SYSTEMS.md` for complete analysis

## Singleton Systems Architecture
- **Massive C++ Architecture** - 80+ singleton patterns identified
- **Sophisticated Design Patterns** - Template-based singleton implementation
- **Professional Game Engine** - Manager, Container, and Factory patterns
- **Advanced Resource Management** - Centralized state and resource coordination
- **Documentation**: See `SINGLETON_SYSTEMS_ANALYSIS.md` for complete analysis

# Kirby Air Ride (GKYE) Decompilation Project

[![Build Status](https://github.com/your-username/kirby-air-ride-decomp/actions/workflows/build.yml/badge.svg)](https://github.com/your-username/kirby-air-ride-decomp/actions/workflows/build.yml)
[![Code Progress](https://decomp.dev/your-username/kirby-air-ride-decomp.svg?mode=shield&measure=code&label=Code)](https://decomp.dev/your-username/kirby-air-ride-decomp)
[![Data Progress](https://decomp.dev/your-username/kirby-air-ride-decomp.svg?mode=shield&measure=data&label=Data)](https://decomp.dev/your-username/kirby-air-ride-decomp)

A work-in-progress decompilation of **Kirby Air Ride** for the Nintendo GameCube.

This repository does **not** contain any game assets or assembly whatsoever. An existing copy of the game is required.

## 🎮 About Kirby Air Ride

Kirby Air Ride is a racing game developed by HAL Laboratory and published by Nintendo for the GameCube in 2003. The game features Kirby riding various air ride machines through colorful tracks, with multiple game modes including:

- **Air Ride Mode** - Traditional racing gameplay
- **Top Ride Mode** - Top-down racing view
- **City Trial Mode** - Open-world exploration and machine building
- **Free Run Mode** - Practice and time trials

## 🚀 Project Status

### Current Progress
- ✅ **DTK Setup Complete** - Build system working, all objects split
- ✅ **gmmain.o Analysis Complete** - All 8 functions identified and named
- ✅ **gmglobal.o Analysis Complete** - All functions identified, transition point found
- ✅ **LAN System Analysis Complete** - Multiplayer networking system documented
- ✅ **HVQM4 Video System Analysis Complete** - Video codec system fully analyzed
- ⏳ **gmautodemo.o Analysis Pending** - Ready to begin analysis
- ⏳ **Remaining Objects** - 142 objects pending analysis

### Build Information
- **Target**: Kirby Air Ride (GameCube, NTSC-U)
- **Game ID**: GKYE
- **Compiler**: Metrowerks CodeWarrior 2.4.2 build 81 (GC MW 1.3.2)
- **Total Objects**: 145 split objects
  - **Game Code**: 48 files (0.00% matched)
  - **SDK Code**: 86 files (0.00% matched)

## 📋 Supported Versions

- `GKYE`: Rev 0 (USA/NTSC-U)

## 🛠️ Dependencies

### Windows
On Windows, it's **highly recommended** to use native tooling. WSL or msys2 are **not** required.

- Install [Python](https://www.python.org/downloads/) and add it to `%PATH%`
  - Also available from the [Windows Store](https://apps.microsoft.com/store/detail/python-311/9NRWMJP3717K)
- Download [ninja](https://github.com/ninja-build/ninja/releases) and add it to `%PATH%`
  - Quick install via pip: `pip install ninja`

### macOS
- Install [ninja](https://github.com/ninja-build/ninja/wiki/Pre-built-Ninja-packages):
  ```sh
  brew install ninja
  ```
- Install [wine-crossover](https://github.com/Gcenx/homebrew-wine):
  ```sh
  brew install --cask --no-quarantine gcenx/wine/wine-crossover
  ```

### Linux
- Install [ninja](https://github.com/ninja-build/ninja/wiki/Pre-built-Ninja-packages)
- For non-x86(_64) platforms: Install wine from your package manager
- For x86(_64), [wibo](https://github.com/decompals/wibo) will be automatically downloaded and used

## 🏗️ Building

### Prerequisites
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/kirby-air-ride-decomp.git
   cd kirby-air-ride-decomp
   ```

2. Copy your game's disc image to `orig/GKYE`
   - Supported formats: ISO (GCM), RVZ, WIA, WBFS, CISO, NFS, GCZ, TGC
   - After the initial build, the disc image can be deleted to save space

### Build Process
1. Configure the project:
   ```sh
   python configure.py
   ```
   To use a version other than `GKYE` (USA), specify it with `--version`

2. Build the project:
   ```sh
   ninja
   ```

## 🔍 Analysis Tools

### DTK (Decomp Toolkit)
This project uses [decomp-toolkit](https://github.com/encounter/decomp-toolkit) for:
- Automatic DOL splitting into relocatable objects
- Symbol management and analysis
- Build system generation
- Progress tracking

### Ghidra Integration
- Function analysis and renaming
- Cross-reference tracking
- Decompilation analysis
- Symbol management

### Objdiff
- Local diffing tool for comparing decompiled code
- Automatic rebuilds on project changes
- Visual diff interface

## 📚 Documentation

### Project Documentation
- [**Decompilation Progress**](docs/DECOMP_PROGRESS.md) - Overall project status and build info
- [**Object Analysis**](docs/OBJECT_ANALYSIS.md) - Detailed analysis of individual object files
- [**LAN System Analysis**](docs/LAN_ANALYSIS.md) - Multiplayer networking system documentation
- [**HVQM4 Video System**](docs/HVQM4_ANALYSIS.md) - Video codec system analysis
- [**Assert String Analysis**](docs/ASSERT_ANALYSIS.md) - Source file mapping and function identification
- [**SDK Functions**](docs/SDK_FUNCTIONS.md) - Identified Dolphin SDK functions
- [**TODO Tasks**](docs/TODO_TASKS.md) - Current and completed tasks

### Technical Documentation
- [**Getting Started**](docs/getting_started.md) - Setup and configuration guide
- [**Dependencies**](docs/dependencies.md) - Detailed dependency information
- [**Symbols.txt**](docs/symbols.md) - Symbol file format and usage
- [**Splits.txt**](docs/splits.txt) - Memory section definitions

## 🏗️ Project Structure

```
KAR-2025/
├── config/GKYE/           # Game-specific configuration
│   ├── config.yml         # DTK configuration
│   ├── symbols.txt        # Function and data symbols
│   ├── splits.txt         # Memory section definitions
│   └── build.sha1         # Expected output checksum
├── docs/                  # Project documentation
├── src/                   # C/C++ source files
├── include/               # C/C++ header files
├── configure.py           # Build system configuration
├── build.ninja           # Generated build file
└── tools/                 # Build tools and scripts
```

## 🎯 Key Features

### Game Systems Analyzed
- **Core Game Loop** - Main game initialization and management
- **LAN Multiplayer** - 12-state menu system, network functions, 4-player support
- **HVQM4 Video System** - Nintendo's proprietary video codec (version 1.5)
- **Memory Management** - Arena-based allocation, debug level support
- **Input System** - Pad initialization, rumble support, input handling

### Technical Achievements
- **145 Objects Split** - Complete DOL decomposition
- **Function Identification** - Key functions named and documented
- **System Architecture** - Understanding of game's internal structure
- **SDK Integration** - Dolphin SDK function mapping
- **Error Handling** - Comprehensive error code analysis

## 🤝 Contributing

We welcome contributions! Here are some ways to help:

### For Beginners
- **Function Analysis** - Help identify and document functions
- **Documentation** - Improve existing documentation
- **Testing** - Verify builds and report issues

### For Experienced Developers
- **Code Decompilation** - Work on matching functions
- **System Analysis** - Analyze game systems and mechanics
- **Tool Development** - Improve analysis tools and scripts

### Getting Started
1. Join our [Discord server](https://discord.gg/hKx3FJJgrV) for help and discussion
2. Check the [TODO list](docs/TODO_TASKS.md) for current tasks
3. Read the [getting started guide](docs/getting_started.md)
4. Start with simple functions and work your way up

## 🔗 Useful Links

### Community
- [**Discord: GC/Wii Decompilation**](https://discord.gg/hKx3FJJgrV) - Come to `#dtk` for help!
- [**decomp.dev**](https://decomp.dev) - Decompilation progress hub and API

### Tools
- [**objdiff**](https://github.com/encounter/objdiff) - Local diffing tool
- [**decomp.me**](https://decomp.me) - Collaborate on matches
- [**wibo**](https://github.com/decompals/wibo) - Minimal Win32 wrapper for Linux
- [**sjiswrap**](https://github.com/encounter/sjiswrap) - UTF-8 to Shift JIS wrapper

### References
- [**decomp-toolkit**](https://github.com/encounter/decomp-toolkit) - Project framework
- [**Active GC/Wii Projects**](https://decomp.dev) - Other decompilation projects

## 📄 License

This project is licensed under the CC0 license. See [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- **HAL Laboratory** - For creating this amazing game
- **Nintendo** - For the GameCube platform and development tools
- **decomp-toolkit team** - For the excellent decompilation framework
- **GC/Wii decompilation community** - For ongoing support and collaboration

---

**Note**: This is a research project for educational purposes. All game assets and code remain the property of their respective owners.

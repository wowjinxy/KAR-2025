# Dolphin SDK Function Mapping

## Identified SDK Functions

### OS (Operating System)
- `OSGetResetCode` (`0x803D89CC`) - Get console reset code
- `OSRegisterVersion` (`0x803D2E08`) - Register version info
- `OSReport` (`0x803D4CE8`) - Debug output/logging
- `OSGetConsoleSimulatedMemSize` (`0x803D7B3C`) - Get console memory size
- `OSAllocFromArenaHi` (`0x803D3C30`) - Allocate from high memory arena
- `OSGetArenaLo` (`0x803D3BEC`) - Get low arena boundary

### PAD (Controller)
- `PADInit` (`0x803DC6D0`) - Initialize controller system
- `PADSetSpec` (`0x803DCD58`) - Set controller specifications

### HSD (HAL Studio)
- `HSD_PadInit` (`0x80414148`) - HAL Studio pad initialization
- `HSD_PadRumbleInit` (`0x80414CB0`) - HAL Studio rumble initialization
- `HSD_Panic` (`0x80428514`) - HAL Studio panic/error handler

### VI (Video Interface)
- `VIInit` (`0x803DDCB4`) - Initialize video interface
- `VIWaitForRetrace` (`0x803DE164`) - Wait for video retrace

### CARD (Memory Card)
- `CARDInit` (`0x803E2C9C`) - Initialize memory card system
- `CARDProbeEx` (`0x803E5C88`) - Extended memory card detection

### DVD
- `DVDConvertPathToEntrynum` (`0x803C4ED4`) - Convert file path to entry number

### AX (Audio)
- `AXStream_main` (`0x8007CE70`) - Audio streaming main function

### Debug/Assert
- `__assert` (`0x804284B8`) - Standard assertion function

### ARAM (Audio RAM)
- `ARAM_Size` (`0x8005811C`) - Get ARAM size information

## Memory Layout
- **SDK Functions**: Generally in `0x803XXXXX` range
- **HSD Functions**: Generally in `0x804XXXXX` range
- **Game Functions**: Generally in `0x8000XXXX` and `0x8005XXXX` ranges

## Usage Patterns
- Most SDK functions are called during `GameMain()` initialization
- Debug functions (`OSReport`, `__assert`) used throughout game code
- Memory management functions used for arena setup
- Controller/input functions initialized early in boot process

## Notes
- Function names follow Nintendo's SDK naming conventions
- Many functions have scope markers (global/local) in symbols.txt
- Some functions may have different signatures than standard SDK docs due to game-specific usage


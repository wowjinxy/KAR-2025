# Object File Analysis

## Linking Order
Based on DTK build report (`build/GKYE/report.json`):

1. **auto_12_805E62E0_sbss2** - Auto-generated section
2. **auto_11_805DE700_sdata2** - Auto-generated section  
3. **auto_10_805DD520_sbss** - Auto-generated section
4. **auto_10_805DDE68_sbss** - Auto-generated section
5. **auto_09_805D50E0_sdata** - Auto-generated section
6. **auto_08_80535300_bss** - Auto-generated section
7. **auto_07_80494E60_data** - Auto-generated section
8. **auto_06_80489480_rodata** - Auto-generated section
9. **gmmain** ✅ - Main game initialization
10. **gmglobal** 🔄 - Global state management
11. **gmautodemo** ⏳ - Auto-demo system
12. **gmracecommon** ⏳ - Common race functionality
13. **gmracenormal** ⏳ - Normal race mode
14. **gmdialogue** ⏳ - Dialogue system
15. **gmdialoguesub** ⏳ - Dialogue subsystem
16. **gmdialoguestatus** ⏳ - Dialogue status
17. **gmspecialmovie** ⏳ - Special movie playback
18. **gmclearchecker** ⏳ - Clear checker system
19. **gmviconfigure** ⏳ - Victory configuration
20. **gmlanmenu** ⏳ - LAN menu

## Object File Details

### gmmain.o ✅ COMPLETE
**Address Range**: `0x80005800` - `0x80005DCC`
**File**: `gmmain.c`
**Purpose**: Main game initialization and entry point

**Functions**:
- `Pad_InitCallback` (`0x80005800`) - Pad initialization callback
- `GameMain` (`0x80005898`) - Main game initialization function
- `GetGlobalDataOffset` (`0x80005CBC`) - Global data pointer offset
- `GetGlobalDataValue` (`0x80005CE0`) - Global data value getter
- `ProcessGlobalDataBits` (`0x80005D04`) - Global data bit processing
- `GetGlobalDataByte` (`0x80005D54`) - Global data byte getter
- `gmSetFreezeGameFlag` (`0x80005D78`) - Set game freeze flag
- `gmUnsetFreezeGameFlag` (`0x80005DCC`) - Clear game freeze flag

**Key Global Variables**:
- `gDebugLevel` (`0x805DD630`) - Debug level (0, 1, 3+)
- `gDbHideForceTurnOn` (`0x805DD634`) - Debug hide force turn on flag
- `gE3BuildFlag` (`0x805DD638`) - E3 build flag
- `gArenaSize` (`0x805DD520`) - Memory arena size

### gmglobal.o ✅ COMPLETE
**Address Range**: `0x8000773C` - `0x8000DFFF`
**File**: `gmglobal.c`
**Purpose**: Global game state management

**Functions Identified**:
- `GetGlobalDataPointer` (`0x8000773C`) - Returns global data pointer
- `GetClearCheckerValue` (`0x8000775C`) - Clear checker system value getter
- `GetIndexedDataByte` (`0x800077F0`) - Indexed data byte getter
- `InitAllSystems` (`0x80007808`) - Initialize all game systems
- `ResetGlobalSystems` (`0x80007840`) - Reset global systems
- `InitSystem1` (`0x80007884`) - Initialize system 1
- `InitSystem2WithUnlocks` (`0x800078E4`) - Initialize system 2 with unlock handling
- `FUN_8000b024` (`0x8000b024`) - Comparison function for unlock checks
- `FUN_8000b884` (`0x8000b884`) - Simple initialization function
- `FUN_8000bd6c` (`0x8000bd6c`) - Global data access function
- `FUN_8000c148` (`0x8000c148`) - Unlock availability check function
- `FUN_8000cd68` (`0x8000cd68`) - Reset code processing function
- `FUN_8000d26c` (`0x8000d26c`) - Complex game initialization orchestration
- **Transition Point**: `0x8000E108` - Start of `gmautodemo.o`

**System Types**:
- Clear checker system (types 0, 1, 2)
- Unlock/achievement system
- Time tracking (possibly for auto-demo idle detection)
- Game mode state management
- Player/character data setup (end of object)

### gmautodemo.o ⏳ PENDING
**Purpose**: Auto-demo system for title screen idle timeout
**Expected Features**:
- Idle time detection on title screen
- CPU-only race initialization
- Demo gameplay logic
- Transition back to title screen

## Notes
- Objects use consistent naming pattern: `gm[system]`
- Many functions reference "gmglobal.c" in assert messages
- Clear separation between initialization, state management, and gameplay objects

# GMLANMENU Function Naming Scheme

## 🏷️ **Function Naming Based on Existing Code Style**

This document provides a comprehensive naming scheme for all functions in `gmlanmenu.o` (0x8004F85C - 0x80054904), following the existing naming conventions found in the Kirby Air Ride codebase.

## **Naming Convention Analysis**

### **Existing Patterns Found:**
- **`gm*`** - Game manager functions (e.g., `gmSetFreezeGameFlag`, `gmGetGlobalP`)
- **`menu*`** - Menu system functions (e.g., `menuGetNextMenuID`, `menu_getCurrentMenuID`)
- **`*Init*`** - Initialization functions (e.g., `Pad_InitCallback`, `TRKInitializeEventQueue`)
- **`*Load*`** - Loading functions (e.g., `__fstLoad`, `TRKLoadContext`)
- **`*Setup*`** - Setup functions (e.g., `__GXInitGX`, `GXInitFifoBase`)
- **`*Update*`** - Update functions (e.g., `GameEffect_UpdateAllEffects`)
- **`*Render*`** - Rendering functions (e.g., `GameEffect_RenderMain`)
- **`*Cleanup*`** - Cleanup functions (e.g., cleanup patterns in other objects)

## **Complete Function Naming Scheme**

### **1. Core LAN Menu Functions (Priority 1)**

```
0x8004F85C - gmLanMenu_Initialize (size: 0x1DC)
0x8004FA38 - gmLanMenu_LoadSceneModels (size: 0x210)
0x8004FC48 - gmLanMenu_SetupUIElements (size: 0x1E0)
0x8004FE28 - gmLanMenu_LoadMenuData (size: 0x284)
0x800500AC - gmLanMenu_SetupNetwork (size: 0x244)
0x800502F0 - gmLanMenu_InitializeStateMachine (size: 0x224)
0x80050514 - gmLanMenu_LoadPlayerData (size: 0x2D8)
0x800507EC - gmLanMenu_SetupConnection (size: 0x254)
0x80050A40 - gmLanMenu_LoadGameModes (size: 0x210)
0x80050C50 - gmLanMenu_SetupRaceConfig (size: 0x258)
0x80050EA8 - gmLanMenu_LoadRaceData (size: 0x180)
0x80051028 - gmLanMenu_StateMachine (size: 0xA7C) ← MAIN FUNCTION
```

### **2. State Machine Handler Functions (Priority 2)**

```
0x80051AA4 - gmLanMenu_HandleStateTransition (size: 0x210)
0x80051CB4 - gmLanMenu_ProcessStateInput (size: 0xC8)
0x80051D7C - gmLanMenu_UpdateState (size: 0x20)
0x80051D9C - gmLanMenu_HandlePlayerJoin (size: 0xA8)
0x80051E44 - gmLanMenu_HandlePlayerLeave (size: 0xA8)
0x80051EEC - gmLanMenu_HandleGameStart (size: 0xAC)
0x80051F98 - gmLanMenu_HandleGameEnd (size: 0x60)
0x80051FF8 - gmLanMenu_HandleError (size: 0x30)
```

### **3. UI and Scene Management (Priority 3)**

```
0x80052028 - gmLanMenu_LoadUIScene (size: 0x290)
0x800522B8 - gmLanMenu_SetupUIRendering (size: 0x214)
0x800524CC - gmLanMenu_UpdateUIScene (size: 0xF0)
0x800525BC - gmLanMenu_RenderUIScene (size: 0x288)
0x80052844 - gmLanMenu_HandleUIInput (size: 0xA8)
0x800528EC - gmLanMenu_UpdateUIState (size: 0x4)
0x800528F0 - gmLanMenu_ProcessUIControls (size: 0xA8)
0x80052998 - gmLanMenu_UpdateUIPosition (size: 0x4)
```

### **4. Network and Connection Management (Priority 4)**

```
0x8005299C - gmLanMenu_InitializeNetwork (size: 0x2A4)
0x80052C40 - gmLanMenu_CheckNetworkStatus (size: 0x18)
0x80052C58 - gmLanMenu_ValidateConnection (size: 0x34)
0x80052C8C - gmLanMenu_TestNetworkLatency (size: 0x18)
0x80052CA4 - gmLanMenu_SetupNetworkBuffers (size: 0x2A4)
0x80052F48 - gmLanMenu_ConfigureNetwork (size: 0x34)
0x80052F7C - gmLanMenu_TestNetworkConnection (size: 0x3C)
0x80052FB8 - gmLanMenu_HandleNetworkEvents (size: 0x788)
```

### **5. Player Management and Synchronization (Priority 5)**

```
0x80053740 - gmLanMenu_UpdatePlayerList (size: 0x18)
0x80053758 - gmLanMenu_SyncPlayerData (size: 0x18)
0x80053770 - gmLanMenu_ValidatePlayerCount (size: 0x3C)
0x800537AC - gmLanMenu_HandlePlayerSynchronization (size: 0x788)
0x80053F34 - gmLanMenu_SetupPlayerBuffers (size: 0x3EC)
0x80054320 - gmLanMenu_UpdatePlayerStates (size: 0xF4)
0x80054414 - gmLanMenu_HandlePlayerInput (size: 0x168)
0x8005457C - gmLanMenu_ProcessPlayerActions (size: 0x114)
```

### **6. Game Mode and Race Configuration (Priority 6)**

```
0x80054690 - gmLanMenu_LoadRaceConfiguration (size: 0x108)
0x80054798 - gmLanMenu_SetupRaceParameters (size: 0x48)
0x800547E0 - gmLanMenu_ValidateRaceSettings (size: 0x124)
0x80054904 - gmLanMenu_FinalizeRaceSetup (size: 0x9C)
```

### **7. Utility and Helper Functions (Priority 7)**

```
0x8004F03C - gmLanMenu_UtilityFunction1 (size: 0x234)
0x8004F270 - gmLanMenu_UtilityFunction2 (size: 0xCC)
0x8004F33C - gmLanMenu_HelperFunction1 (size: 0x20)
0x8004F35C - gmLanMenu_HelperFunction2 (size: 0x20)
0x8004F37C - gmLanMenu_HelperFunction3 (size: 0x20)
0x8004F39C - gmLanMenu_UtilityFunction3 (size: 0x28)
0x8004F3C4 - gmLanMenu_HelperFunction4 (size: 0x54)
0x8004F418 - gmLanMenu_UtilityFunction4 (size: 0x3C)
0x8004F454 - gmLanMenu_HelperFunction5 (size: 0x15C)
0x8004F5B0 - gmLanMenu_UtilityFunction5 (size: 0x20)
0x8004F5D0 - gmLanMenu_HelperFunction6 (size: 0x10)
0x8004F5E0 - gmLanMenu_UtilityFunction6 (size: 0x74)
0x8004F654 - gmLanMenu_HelperFunction7 (size: 0xC0)
0x8004F714 - gmLanMenu_UtilityFunction7 (size: 0x68)
0x8004F77C - gmLanMenu_HelperFunction8 (size: 0xC0)
0x8004F83C - gmLanMenu_UtilityFunction8 (size: 0x20)
```

## **Function Size Analysis**

### **Large Functions (>0x200 bytes)**
- **`gmLanMenu_StateMachine`** - 0xA7C (2,684 bytes) - Main state machine
- **`gmLanMenu_HandleNetworkEvents`** - 0x788 (1,928 bytes) - Network event handling
- **`gmLanMenu_HandlePlayerSynchronization`** - 0x788 (1,928 bytes) - Player sync
- **`gmLanMenu_LoadUIScene`** - 0x290 (656 bytes) - UI scene loading
- **`gmLanMenu_SetupPlayerBuffers`** - 0x3EC (1,004 bytes) - Player buffer setup

### **Medium Functions (0x100-0x200 bytes)**
- **`gmLanMenu_LoadSceneModels`** - 0x210 (528 bytes)
- **`gmLanMenu_SetupUIElements`** - 0x1E0 (480 bytes)
- **`gmLanMenu_LoadMenuData`** - 0x284 (644 bytes)
- **`gmLanMenu_SetupNetwork`** - 0x244 (580 bytes)
- **`gmLanMenu_InitializeStateMachine`** - 0x224 (548 bytes)

### **Small Functions (<0x100 bytes)**
- **`gmLanMenu_UpdateState`** - 0x20 (32 bytes)
- **`gmLanMenu_CheckNetworkStatus`** - 0x18 (24 bytes)
- **`gmLanMenu_UpdateUIState`** - 0x4 (4 bytes)
- **`gmLanMenu_UpdateUIPosition`** - 0x4 (4 bytes)

## **Function Grouping by Responsibility**

### **Initialization Group**
```
gmLanMenu_Initialize
gmLanMenu_LoadSceneModels
gmLanMenu_SetupUIElements
gmLanMenu_LoadMenuData
gmLanMenu_SetupNetwork
gmLanMenu_InitializeStateMachine
```

### **State Management Group**
```
gmLanMenu_StateMachine (MAIN)
gmLanMenu_HandleStateTransition
gmLanMenu_ProcessStateInput
gmLanMenu_UpdateState
```

### **Player Management Group**
```
gmLanMenu_HandlePlayerJoin
gmLanMenu_HandlePlayerLeave
gmLanMenu_UpdatePlayerList
gmLanMenu_SyncPlayerData
gmLanMenu_ValidatePlayerCount
gmLanMenu_HandlePlayerSynchronization
```

### **Network Management Group**
```
gmLanMenu_SetupNetwork
gmLanMenu_CheckNetworkStatus
gmLanMenu_ValidateConnection
gmLanMenu_TestNetworkLatency
gmLanMenu_SetupNetworkBuffers
gmLanMenu_HandleNetworkEvents
```

### **UI Management Group**
```
gmLanMenu_LoadUIScene
gmLanMenu_SetupUIRendering
gmLanMenu_UpdateUIScene
gmLanMenu_RenderUIScene
gmLanMenu_HandleUIInput
gmLanMenu_ProcessUIControls
```

### **Game Configuration Group**
```
gmLanMenu_LoadGameModes
gmLanMenu_SetupRaceConfig
gmLanMenu_LoadRaceData
gmLanMenu_LoadRaceConfiguration
gmLanMenu_SetupRaceParameters
gmLanMenu_ValidateRaceSettings
gmLanMenu_FinalizeRaceSetup
```

## **Implementation Priority for Custom Server**

### **Phase 1: Core Network Functions**
1. **`gmLanMenu_SetupNetwork`** - Replace with server connection
2. **`gmLanMenu_HandleNetworkEvents`** - Add server event handling
3. **`gmLanMenu_ValidateConnection`** - Add server validation

### **Phase 2: State Machine Extensions**
1. **`gmLanMenu_StateMachine`** - Add server mode states
2. **`gmLanMenu_HandleStateTransition`** - Handle server transitions
3. **`gmLanMenu_ProcessStateInput`** - Process server input

### **Phase 3: Player Management Extensions**
1. **`gmLanMenu_HandlePlayerJoin`** - Handle server player joins
2. **`gmLanMenu_HandlePlayerSynchronization`** - Server player sync
3. **`gmLanMenu_ValidatePlayerCount`** - Extended player count validation

### **Phase 4: UI Extensions**
1. **`gmLanMenu_LoadUIScene`** - Add server UI elements
2. **`gmLanMenu_SetupUIElements`** - Server UI configuration
3. **`gmLanMenu_HandleUIInput`** - Server UI input handling

## **Naming Convention Summary**

### **Prefix Pattern: `gmLanMenu_`**
- **Consistent with existing `gm*` functions**
- **Clear identification as LAN menu functions**
- **Easy to search and filter**

### **Function Type Suffixes:**
- **`*Initialize`** - Initialization functions
- **`*Load*`** - Loading and setup functions
- **`*Setup*`** - Configuration functions
- **`*Handle*`** - Event handling functions
- **`*Update*`** - Update and processing functions
- **`*Render*`** - Rendering functions
- **`*Validate*`** - Validation functions
- **`*Process*`** - Data processing functions

### **Size-Based Naming:**
- **Large functions** get descriptive names
- **Medium functions** get functional names
- **Small functions** get concise names
- **Utility functions** get generic names

## **Benefits of This Naming Scheme**

1. **Consistency** - Follows existing codebase patterns
2. **Clarity** - Function purpose is immediately clear
3. **Searchability** - Easy to find related functions
4. **Maintainability** - Clear organization and grouping
5. **Extensibility** - Easy to add new server-related functions

## **Next Steps**

1. **Apply names to symbols.txt** - Update function references
2. **Update documentation** - Reference new function names
3. **Implement custom server** - Use named functions as hook points
4. **Maintain consistency** - Follow naming scheme for new functions

---

**Created**: [Current Date]
**Status**: Naming Scheme Complete
**Priority**: High
**Use Case**: Custom Server Implementation
**Complexity**: Low
**Risk Level**: None

# LAN Code Location Map in DOL File

## 🗺️ **Complete LAN Code Memory Layout**

This document maps out exactly where all the LAN (Local Area Network) multiplayer code is located in the Kirby Air Ride DOL file. This information is crucial for reverse engineering, patching, and implementing custom server modifications.

## **Memory Section Overview**

### **Text Section (Code)**
- **`.text`** - Main executable code (0x80005800 - 0x803AE1BC)
- **`.init`** - Initialization code (0x80003238 - 0x80003100)

### **Data Sections**
- **`.data`** - Read-write data (0x80497BB8, 0x804AD688, 0x804AD6B8)
- **`.sdata`** - Small read-write data (0x805D540C)
- **`.rodata`** - Read-only data
- **`.bss`** - Uninitialized data

## **LAN Code Object Locations**

### **1. Main LAN Menu System (`gmlanmenu.o`)**
```
Object: gmlanmenu.o
Section: .text
Memory Range: 0x8004F85C - 0x80054904
Size: 0x50A8 (20,648 bytes)
```

**Key Functions in gmlanmenu.o:**
- **`fn_80051028`** @ `0x80051028` - Main LAN menu state machine (size: 0xA7C)
  - Handles 12 different LAN menu states
  - Core multiplayer connection logic
  - Game mode selection and player management

### **2. LAN Number Selection (`mnlannumber.c`)**
```
Object: text_801166B4.o (contains mnlannumber functions)
Section: .text
Memory Range: 0x801166B4 - 0x801D443C
Size: 0xCDD88 (843,656 bytes)
```

**Key Functions in mnlannumber.c:**
- **`fn_80183878`** @ `0x80183878` - LAN number scene model loading (size: 0x4C)
- **`fn_801838C4`** @ `0x801838C4` - LAN number UI setup (size: 0xD0)
- **`fn_8018352C`** @ `0x8018352C` - Render first option (size: 0xB4)
- **`fn_801835E0`** @ `0x801835E0` - Render second option (size: 0xB4)
- **`fn_80183694`** @ `0x80183694` - Render third option (size: 0xB4)
- **`fn_80183250`** @ `0x80183250` - Cleanup resources (size: 0x44)
- **`fn_80183994`** @ `0x80183994` - Cleanup UI (size: 0x44)

**Initialization Function:**
- **`mnlannumber.cmemset`** @ `0x80003100` - Memory initialization (size: 0x30)

### **3. LAN Dialogue System (`mnlandialogue.c`)**
```
Data References:
- 0x804AD688 - Scene model data (size: 0x10)
- 0x804AD6B8 - Scene model data (size: 0x10)
```

### **4. Network Library Functions (`lbnet.c`)**
```
Data References:
- 0x805D540C - Network library data (size: 0x8)
```

**Key Network Functions:**
- **`fn_8007B820`** @ `0x8007B820` - Network initialization (size: 0x20)
- **`fn_8007B860`** @ `0x8007B860` - Network communication (size: 0x20)
- **`fn_8007B880`** @ `0x8007B880` - Network cleanup (size: 0x54)
- **`fn_8007B934`** @ `0x8007B934` - Network status check (size: 0x20)
- **`fn_8007B954`** @ `0x8007B954` - Connection state check (size: 0x3C)
- **`fn_8007CE14`** @ `0x8007CE14` - Connection validation (size: 0x20)
- **`fn_8007CE34`** @ `0x8007CE34` - Connection establishment (size: 0x20)

### **5. Player Management Functions**
```
Object: gmglobal.o (contains player management)
Section: .text
Memory Range: 0x80005CBC - 0x8000E1D8
```

**Key Player Functions:**
- **`getPlayerCount`** @ `0x800092B4` - Player count retrieval (size: 0x24)

## **Memory Layout Visualization**

```
DOL Memory Layout (LAN Code Focus)
┌─────────────────────────────────────────────────────────────┐
│                    .text Section                           │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 0x80005800 - 0x80005CBC: gmmain.o                  │   │
│  │ 0x80005CBC - 0x8000E1D8: gmglobal.o                │   │
│  │ 0x8004F85C - 0x80054904: gmlanmenu.o ← LAN MENU    │   │
│  │ 0x80054904 - 0x80060ED0: lbairride.o                │   │
│  │ 0x80060ED0 - 0x800AD79C: text_80060ED0.o            │   │
│  │ 0x800AD79C - 0x800AEBDC: db_800AD79C.o              │   │
│  │ 0x800AEBDC - 0x800AF474: smsoundtest.o              │   │
│  │ 0x800AF474 - 0x8010F114: text_800AF474.o            │   │
│  │ 0x8010F114 - 0x8010F854: grcity1.o                  │   │
│  │ 0x8010F854 - 0x801166B4: text_800AF474.o            │   │
│  │ 0x801166B4 - 0x801D443C: text_801166B4.o ← LAN NUM │   │
│  │ 0x801D443C - 0x802894BC: text_801D443C.o            │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    .data Section                          │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 0x80497BB8: gmlanmenu scene data (size: 0xC)       │   │
│  │ 0x804AD688: mnlandialogue scene data (size: 0x10)  │   │
│  │ 0x804AD6B8: mnlandialogue scene data (size: 0x10)  │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    .sdata Section                         │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 0x805D540C: lbnet network library data (size: 0x8)│   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

## **Function Address Mapping**

### **Core LAN Functions (Priority 1)**
```
0x80051028 - Main LAN menu state machine (gmlanmenu.o)
0x8007B820 - Network initialization (lbnet.c)
0x8007B860 - Network communication (lbnet.c)
0x8007B880 - Network cleanup (lbnet.c)
0x8007B934 - Network status check (lbnet.c)
0x8007B954 - Connection state check (lbnet.c)
0x8007CE14 - Connection validation (lbnet.c)
0x8007CE34 - Connection establishment (lbnet.c)
```

### **LAN UI Functions (Priority 2)**
```
0x80183878 - LAN number scene loading (mnlannumber.c)
0x801838C4 - LAN number UI setup (mnlannumber.c)
0x8018352C - Render first option (mnlannumber.c)
0x801835E0 - Render second option (mnlannumber.c)
0x80183694 - Render third option (mnlannumber.c)
0x80183250 - Cleanup resources (mnlannumber.c)
0x80183994 - Cleanup UI (mnlannumber.c)
```

### **Player Management Functions (Priority 3)**
```
0x800092B4 - getPlayerCount (gmglobal.o)
```

### **Data References (Priority 4)**
```
0x80497BB8 - gmlanmenu scene data
0x804AD688 - mnlandialogue scene data
0x804AD6B8 - mnlandialogue scene data
0x805D540C - lbnet network library data
```

## **Object File Dependencies**

### **gmlanmenu.o Dependencies**
- **Scene Models**: 0x80497BB8 (LAN menu scene data)
- **Network Functions**: Calls lbnet.c functions
- **Player Management**: Integrates with gmglobal.o

### **mnlannumber.c Dependencies**
- **Scene Models**: 0x804AD688, 0x804AD6B8
- **Memory Management**: 0x80003100 (initialization)
- **UI System**: HAL scene model system

### **lbnet.c Dependencies**
- **Network Data**: 0x805D540C
- **System Calls**: GameCube network card functions
- **Error Handling**: LbNetError enumeration

## **Reverse Engineering Strategy**

### **Phase 1: Core LAN Functions**
1. **Analyze `fn_80051028`** - Main state machine
2. **Study network functions** - 0x8007B820-0x8007CE34
3. **Map state transitions** - 12-state menu system

### **Phase 2: UI and Scene Systems**
1. **Examine mnlannumber.c** - Player count selection
2. **Study scene models** - 3D UI rendering
3. **Map UI interactions** - Menu navigation

### **Phase 3: Data Structures**
1. **Analyze network data** - 0x805D540C
2. **Study scene data** - 0x80497BB8, 0x804AD688
3. **Map memory layout** - Buffer allocations

### **Phase 4: Integration Points**
1. **Player management** - getPlayerCount integration
2. **Game mode systems** - Race configuration
3. **Error handling** - Network failure recovery

## **Custom Server Implementation Targets**

### **Primary Hook Points**
```
0x8007B820 - Network initialization (replace with server connection)
0x8007B860 - Network communication (replace with server communication)
0x8007CE14 - Connection validation (add server validation)
0x8007CE34 - Connection establishment (add server establishment)
```

### **Secondary Modification Points**
```
0x80051028 - LAN menu state machine (add server mode states)
0x80183878 - Scene loading (add server UI elements)
0x800092B4 - Player count (extend for server players)
```

### **Data Structure Extensions**
```
0x80497BB8 - Add server configuration data
0x805D540C - Extend network library for server support
```

## **Memory Patching Considerations**

### **Function Hooking Strategy**
1. **Find function addresses** using Ghidra
2. **Create trampoline functions** for server mode
3. **Patch function calls** to redirect to custom code
4. **Maintain fallback** to original LAN functions

### **Data Structure Patching**
1. **Extend existing structures** for server data
2. **Add new data sections** for server configuration
3. **Modify scene models** for server UI elements

### **Compatibility Requirements**
1. **Preserve original LAN mode** functionality
2. **Maintain memory layout** compatibility
3. **Ensure fallback** to LAN if server fails

## **Summary**

The LAN code in Kirby Air Ride is **well-organized** and **modularly structured**:

- **Main LAN System**: `gmlanmenu.o` (0x8004F85C - 0x80054904)
- **Player Selection**: `mnlannumber.c` in `text_801166B4.o` (0x801166B4 - 0x801D443C)
- **Network Functions**: `lbnet.c` functions scattered throughout .text section
- **Data Structures**: Scene models and network data in .data and .sdata sections

This organization makes it **highly feasible** to implement custom server modifications by:
1. **Hooking network functions** at specific addresses
2. **Extending data structures** for server support
3. **Adding new UI elements** for server configuration
4. **Maintaining compatibility** with original LAN mode

The modular design allows for **targeted modifications** without affecting the entire system, making custom server implementation a realistic goal! 🚀

---

**Created**: [Current Date]
**Status**: Analysis Complete
**Priority**: High
**Use Case**: Custom Server Implementation
**Complexity**: Medium
**Risk Level**: Low

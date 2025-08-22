# HVQM4 Video Rendering System Analysis

This document analyzes the HVQM4 (High Quality Video for Multiple 4) video rendering system library in Kirby Air Ride. HVQM4 is Nintendo's proprietary video codec system for the GameCube/Wii platform.

## HVQM4 System Overview

HVQM4 is Nintendo's advanced video codec that provides:
- **High-quality video compression** for cutscenes and movies
- **Hardware acceleration** via the GameCube's video hardware
- **Multiple format support** including 4:2:0 YUV color space
- **Efficient memory management** for video buffers and decoding
- **Threaded playback** for smooth video performance

## Source Files and Structure

### Core HVQM4 Files
- **`lbhvqm.c`** @ `0x8049aa28` - HAL laboratory HVQM4 library wrapper
- **`HVQM4PlayerDx.c`** @ `0x80532418` - Extended HVQM4 player implementation
- **`video.c`** @ `0x805dcc38` - Video system integration

### Version Information
- **HVQM4 Version**: 1.5 (from string `"HVQM4 1.5"` @ `0x805325c8`)

## Core HVQM4 Functions

### Discovered Function Names
Based on assert strings and error messages, we've identified several key HVQM4 functions:

#### **Core Allocation Functions:**
- **`HVQM4Alloc`** - Main memory allocator (function pointer at `0x8045d6a4`)
- **`HVQM4BufvGetFree`** - Get free video buffer from pool
- **`HVQM4Bufv_AllocCircular`** - Allocate circular video buffer system
- **`HVQM4Bufa_AllocCircular`** - Allocate circular audio buffer system

#### **Data Structures:**
- **`hHVQM4PlayerEx`** - Extended HVQM4 player handle
- **`hBufv`** - Video buffer pool handle
- **`buff[0-2].bufv`** - Individual video frame buffers
- **`workbuff`** - Decoding workspace buffer
- **`playerThreadStack`** - Thread execution stack

### Player Initialization and Management

#### **`HVQM4_PlayerEx_Init`** @ `0x8045eb6c` - HVQM4 Player Extended Initialization
This is the main HVQM4 player setup function with extensive error handling:

**Key Features:**
- **Memory Allocation** - Allocates 0x440 bytes for player structure
- **Buffer Management** - Sets up video, audio, and work buffers
- **Thread Creation** - Creates dedicated playback thread
- **Format Detection** - Automatically detects video format and dimensions
- **Error Recovery** - Comprehensive cleanup on initialization failure

**Buffer Setup:**
- **Video Buffers** - 3-frame circular buffer system
- **Audio Buffers** - PCM audio buffer allocation
- **Work Buffer** - Decoding workspace memory
- **Thread Stack** - Dedicated thread execution space

**Error Codes:**
- `0xd` - System disabled
- `2` - File open failure
- `3` - Format detection failure
- `4` - Buffer allocation failure
- `9` - Format unsupported
- `10` - Audio setup failure
- `11` - Audio codec failure

#### **`HVQM4Bufv_AllocCircular`** @ `0x8045d6f4` - Video Buffer Allocator
Manages circular video buffer allocation:

**Features:**
- **Circular Buffer** - Creates linked list of video frames
- **Memory Alignment** - Ensures 32-byte alignment for DMA
- **Frame Linking** - Links frames in circular pattern
- **Size Calculation** - Computes buffer sizes based on video dimensions

#### **`HVQM4Bufa_AllocCircular`** @ `0x8045dae4` - Audio Buffer Allocator
Manages circular audio buffer allocation:

**Features:**
- **Circular Buffer** - Creates linked list of audio buffers
- **Memory Alignment** - Ensures 32-byte alignment for audio hardware
- **Buffer Linking** - Links audio buffers in circular pattern
- **Size Optimization** - Calculated based on audio duration and sample rate

#### **`HVQM4Bufv_GetFree`** @ `0x8045d8e0` - Get Free Video Buffer
Retrieves available video buffer from the pool:

**Features:**
- **Buffer Pool Management** - Manages available video buffers
- **Thread Safety** - Uses critical sections for thread-safe access
- **Circular Management** - Maintains circular buffer structure
- **Resource Tracking** - Tracks buffer availability and usage

#### **`HVQM4Audio_InitCodec`** @ `0x80465cc0` - Audio Codec Initialization
Sets up the audio codec for HVQM4 playback:

**Features:**
- **Codec Setup** - Initializes audio decoding parameters
- **Memory Allocation** - Allocates codec workspace (0x24 bytes)
- **Parameter Configuration** - Sets up sample rate and format
- **Error Handling** - Graceful failure on allocation errors

### HAL Library Integration

#### **`HAL_HVQM4_Init`** @ `0x80077980` - HAL HVQM4 Initialization
Sets up the HAL laboratory HVQM4 system:

**Functions:**
- **Display Stack** - Allocates video display stack memory
- **Thread Creation** - Creates HVQM4 management thread
- **System State** - Initializes global HVQM4 state variables
- **Memory Management** - Sets up display buffer allocation

**Memory Layout:**
- `0x805dd608` - Display stack pointer
- `0x805dd604` - System active flag
- `0x805dd5e8` - Current state

## Video Format Support

### Supported Formats
Based on the code analysis, HVQM4 supports:

#### **Video Specifications:**
- **Resolution**: Variable (detected from file header)
- **Color Space**: 4:2:0 YUV (YUV420)
- **Frame Rate**: Variable (detected from file)
- **Compression**: HVQM4 proprietary codec

#### **Audio Specifications:**
- **Format**: PCM audio
- **Channels**: Stereo (2-channel)
- **Sample Rate**: Variable (detected from file)
- **Bit Depth**: 16-bit

### Format Detection
The system automatically detects:
- Video dimensions (width × height)
- Frame rate and duration
- Audio specifications
- Compression parameters

## Memory Management

### Buffer Architecture

#### **Video Buffer System:**
- **Circular Buffer** - 3-frame rotation system
- **Frame Storage** - Individual frame buffers
- **Memory Alignment** - 32-byte DMA alignment
- **Size Optimization** - Calculated based on video dimensions

#### **Audio Buffer System:**
- **PCM Buffer** - Raw audio data storage
- **Size Calculation** - Based on duration and sample rate
- **Memory Alignment** - Optimized for audio hardware

#### **Work Buffer System:**
- **Decoding Space** - Temporary processing memory
- **Thread Stack** - Execution space for playback thread
- **Alignment** - 32-byte boundary alignment

### Memory Allocation Strategy
- **Dynamic Sizing** - Buffers sized based on content
- **Efficient Use** - Minimal memory overhead
- **Hardware Optimization** - Aligned for DMA operations
- **Cleanup** - Proper deallocation on errors

## Threading and Performance

### Multi-threaded Architecture

#### **Playback Thread:**
- **Dedicated Execution** - Separate thread for video decoding
- **Priority Management** - Controlled thread priority
- **Synchronization** - Thread-safe buffer access
- **Performance** - Optimized for smooth playback

#### **Thread Management:**
- **Creation** - `OSCreateThread` for playback
- **Stack Allocation** - Dedicated stack space
- **Priority Control** - Adjustable thread priority
- **Cleanup** - Proper thread termination

### Performance Optimizations
- **Hardware Acceleration** - Uses GameCube video hardware
- **Buffer Management** - Efficient circular buffer system
- **Memory Alignment** - Optimized for DMA operations
- **Format Detection** - Fast header parsing

## Error Handling and Recovery

### Comprehensive Error System

#### **Error Categories:**
1. **System Errors** - Hardware or system failures
2. **File Errors** - File access or format issues
3. **Memory Errors** - Allocation failures
4. **Format Errors** - Unsupported video/audio formats
5. **Audio Errors** - Audio codec or buffer issues

#### **Recovery Mechanisms:**
- **Automatic Cleanup** - Resource deallocation on errors
- **State Reset** - Return to safe system state
- **Error Reporting** - Detailed error codes for debugging
- **Graceful Degradation** - Continue operation when possible

### Assert System
All critical functions use assert statements:
- **File Validation** - Check file format and integrity
- **Memory Validation** - Verify allocation success
- **State Validation** - Ensure system consistency
- **Parameter Validation** - Verify input parameters

## Integration with Game Systems

### Special Movie System
- **`gmspecialmovie.c`** - Game movie playback integration
- **Scene Models** - `ScMenMovie_scene_models` for UI
- **Test Mode** - "Movie Test" debug functionality

### Video System Integration
- **`video.c`** - Core video system integration
- **Display Management** - Video output coordination
- **Format Support** - Multiple video format handling

## Debug and Development Features

### Test and Debug Modes
- **Movie Test Mode** - Debug video playback
- **Error Reporting** - Detailed error messages
- **State Monitoring** - System state tracking
- **Performance Metrics** - Timing and memory usage

### Development Tools
- **Assert System** - Source file and line tracking
- **Error Codes** - Comprehensive error categorization
- **Memory Tracking** - Allocation and deallocation monitoring
- **Thread Monitoring** - Thread state and performance

## Technical Specifications

### Hardware Requirements
- **GameCube Video Hardware** - Hardware acceleration support
- **Memory Bandwidth** - Sufficient for video streaming
- **CPU Performance** - Multi-threaded decoding support

### Performance Characteristics
- **Frame Rate** - Variable (typically 30fps or 60fps)
- **Resolution** - Variable (typically 320×240 to 640×480)
- **Memory Usage** - Optimized for GameCube memory constraints
- **CPU Usage** - Efficient multi-threaded implementation

## Summary

The HVQM4 system in Kirby Air Ride represents a **sophisticated, production-ready video playback system** that demonstrates:

- **Professional Video Architecture** - Full-featured video codec implementation with proper function naming
- **Hardware Optimization** - Leverages GameCube video hardware capabilities
- **Robust Error Handling** - Comprehensive error recovery and reporting with detailed error codes
- **Performance Optimization** - Multi-threaded architecture for smooth playback
- **Memory Efficiency** - Optimized circular buffer management for limited memory
- **Format Flexibility** - Support for various video and audio specifications
- **SDK Compatibility** - Uses standard HVQM4 function names and data structures

### Key Discoveries from Assert Analysis

By analyzing assert strings and error messages, we've identified the **actual HVQM4 SDK function names** used in the implementation:

- **`HVQM4Alloc`** - Standard memory allocator
- **`HVQM4BufvGetFree`** - Video buffer pool management
- **`hHVQM4PlayerEx`** - Extended player handle structure
- **`hBufv`** - Video buffer pool handle
- **`workbuff`** - Decoding workspace buffer

This system enables Kirby Air Ride to include high-quality video content (cutscenes, intros, outros) while maintaining smooth gameplay performance. The implementation shows Nintendo's expertise in creating efficient multimedia systems for resource-constrained platforms, and the use of standard SDK function names indicates this is a **production-quality implementation** that follows Nintendo's development standards.

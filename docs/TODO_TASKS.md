# TODO Tasks

## Current Tasks
- [x] **Complete gmglobal.o analysis** - Found transition point to gmautodemo.o at 0x8000E108
- [ ] **Update symbols.txt with gmglobal functions** - Add identified function names
- [ ] **Analyze gmautodemo.o** - Identify auto-demo system functions
- [ ] **Binary object integration** - Link rootDesc.xml, debugfont.bin files

## Completed Tasks
- [x] **DTK project setup** - Configure build system with correct compiler flags
- [x] **Fix jump table issues** - Resolved DTK build errors with data splitting
- [x] **gmmain.o complete analysis** - All 8 functions identified and named
- [x] **SDK function identification** - 15+ SDK functions properly named
- [x] **Global variable naming** - Debug level, E3 flag, arena size variables
- [x] **Build verification** - Confirmed DTK build produces correct checksum

## Pending Object Files (143 remaining)
1. **gmautodemo.o** - Auto-demo system
2. **gmracecommon.o** - Common race functionality  
3. **gmracenormal.o** - Normal race mode
4. **gmdialogue.o** - Dialogue system
5. **gmdialoguesub.o** - Dialogue subsystem
6. **gmdialoguestatus.o** - Dialogue status
7. **gmspecialmovie.o** - Special movie playback
8. **gmclearchecker.o** - Clear checker system
9. **gmviconfigure.o** - Victory configuration
10. **gmlanmenu.o** - LAN menu
11. **lbairride.o** - Air ride library
12. **text_*.o** - Various text/data sections
13. **a2d_*.o** - Air ride 2D/game objects
14. **gr*.o** - Graphics objects
15. **SDK objects** - Dolphin SDK components

## Binary Objects Status
- [x] **Located binary files** - debugfont.bin, rootDesc.xml in binObjects/
- [x] **Found addresses** - rootDesc.xml@0x8049ae10, debugfont.bin@0x8050a040, etc.
- [ ] **DTK integration** - Need proper data object linking in symbols.txt

## Quality Goals
- [ ] **100% function coverage** - All functions properly named
- [ ] **Consistent naming** - Follow established patterns
- [ ] **Documentation** - Document system interactions
- [ ] **Build verification** - Maintain byte-exact output

## Notes
- Focus on one object file at a time for systematic progress
- Use assert messages and strings to identify source files
- Verify all changes maintain DTK build integrity
- Update documentation as discoveries are made

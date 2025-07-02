# Multi-Platform Implementation Plan

## Executive Summary

Transform the welcome guide to support Windows, macOS, and Linux while maintaining the achieved 70% content reduction and professional tone. Implementation will use minimal tabs for platform-specific commands and preserve the command-first philosophy.

## Phase 1: Command Inventory ✓ COMPLETE

### Findings
- 25% of commands need platform variations
- Virtual environment activation appears 6 times
- Package manager commands vary by OS
- Git commands are 100% universal

## Phase 2: Pattern Application (2 hours)

### Task 2.1: Transform setup.md
**Priority**: HIGH (most platform variations)
**Word Budget**: +150 words

Commands to transform:
1. Automated setup scripts → Pattern B (Windows/macOS-Linux tabs)
2. Package managers table → Enhance existing table
3. UV installation → Pattern B
4. Git autocrlf → Inline comment approach
5. Virtual environment activation → Pattern B

### Task 2.2: Transform index.md
**Priority**: HIGH (entry point)
**Word Budget**: +100 words

Commands to transform:
1. Fast Track UV installation → Pattern B tabs
2. Fast Track venv activation → Pattern B tabs
3. Prerequisites check → Keep universal

### Task 2.3: Transform reference.md
**Priority**: MEDIUM
**Word Budget**: +150 words

Commands to transform:
1. SSH key setup → Pattern B with path notes
2. Git config section → Improve existing dual display
3. Add platform reference table (new section)

### Task 2.4: Transform workflow.md
**Priority**: LOW (mostly universal)
**Word Budget**: +110 words

Commands to transform:
1. Health check script → Add Windows PowerShell variant
2. Branch operations → Keep universal

## Phase 3: Reference Infrastructure (1 hour)

### Task 3.1: Create Platform Reference Table
Location: reference.md
Content:
- Path conventions
- Shell differences
- Package managers
- Admin privileges

### Task 3.2: Add Platform-Specific Troubleshooting
- Windows: PowerShell execution policy
- macOS: Homebrew installation
- Linux: Package manager selection

### Task 3.3: Update Prerequisites
- Clear OS version requirements
- Shell requirements per platform
- Tool availability matrix

## Phase 4: Validation (1 hour)

### Task 4.1: Command Testing
- [ ] Test all Windows commands in PowerShell
- [ ] Test all Windows commands in Git Bash
- [ ] Test macOS commands in zsh
- [ ] Test Linux commands in bash

### Task 4.2: Content Metrics
- [ ] Verify <20% content increase per page
- [ ] Check readability on mobile
- [ ] Validate tab navigation
- [ ] Confirm copy-paste functionality

### Task 4.3: Time Estimates
- [ ] Verify 45-minute completion remains valid
- [ ] Update estimates if platform steps differ
- [ ] Test Fast Track on each platform

## Implementation Rules

### DO:
- Use Pattern A for universal commands (75%)
- Combine macOS/Linux when identical
- Place platform notes below commands
- Maintain command-first structure
- Keep professional tone

### DON'T:
- Add platform explanations
- Create separate platform pages
- Duplicate universal commands
- Use more than 3 tabs
- Exceed 20% content increase

## Success Metrics

1. **Content Control**
   - Current: 2,550 words
   - Maximum: 3,060 words
   - Target: 2,900 words

2. **Command Discovery**
   - Platform-specific command found in <5 seconds
   - Visual hierarchy maintained
   - Tabs render correctly

3. **User Experience**
   - Copy-paste ready for all platforms
   - Clear platform indicators
   - No navigation confusion

## Rollback Plan

If implementation exceeds constraints:
1. Remove platform reference table (-100 words)
2. Combine more platform variations inline
3. Link to external platform guides
4. Prioritize Windows/macOS only

## Next Steps

1. Begin with setup.md transformation (highest impact)
2. Apply patterns consistently
3. Test on target platforms
4. Measure word count after each file
5. Adjust approach if needed
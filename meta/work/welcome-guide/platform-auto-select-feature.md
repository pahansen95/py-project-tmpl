# Platform Auto-Select Feature

## Overview

Added JavaScript functionality to automatically select the appropriate platform tab based on the user's operating system.

## Implementation

### File: `/docs/javascripts/platform-tabs.js`

Features:
1. **Auto-detection**: Detects Windows vs Unix-like systems (macOS/Linux)
2. **User preference**: Remembers manual tab selections in localStorage
3. **Instant navigation**: Works with MkDocs Material's instant loading feature

### How it works

1. On page load, detects the user's platform using `navigator.platform`
2. Automatically selects the appropriate tab (Windows or macOS/Linux)
3. If user manually selects a different tab, saves this preference
4. Future visits respect the saved preference over auto-detection

### Configuration

Added to `mkdocs.yml`:
```yaml
extra_javascript:
  - javascripts/platform-tabs.js
```

## Benefits

1. **Better UX**: Users see relevant commands immediately
2. **Reduced friction**: No need to manually select platform tabs
3. **Persistent choice**: Respects user preferences if they switch tabs
4. **Seamless experience**: Works across all pages with platform tabs

## Testing

To test the feature:
1. Open the documentation in different browsers/OSes
2. Verify correct tab is auto-selected
3. Manually switch tabs and refresh - preference should persist
4. Clear localStorage to reset: `localStorage.removeItem('preferredPlatform')`
// Auto-select platform tabs based on user's OS
document$.subscribe(function() {
    'use strict';
    
    console.log('[Platform Tabs] Initializing...');
    
    // Flag to prevent saving auto-selections as user preferences
    let isAutoSelecting = false;
    
    // Detect user's platform
    function detectPlatform() {
        const platform = navigator.platform.toLowerCase();
        const userAgent = navigator.userAgent.toLowerCase();
        
        console.log('[Platform Tabs] Detected platform:', platform);
        
        if (platform.includes('win') || userAgent.includes('windows')) {
            return 'windows';
        }
        return 'unix';
    }
    
    // Select appropriate tabs based on platform
    function selectPlatformTabs() {
        const platform = detectPlatform();
        const savedPlatform = localStorage.getItem('preferredPlatform');
        const targetPlatform = savedPlatform || platform;
        
        console.log('[Platform Tabs] Target platform:', targetPlatform);
        
        // Set flag to prevent auto-selections from being saved
        isAutoSelecting = true;
        
        // MkDocs Material tab structure
        const tabGroups = document.querySelectorAll('.tabbed-set');
        console.log('[Platform Tabs] Found', tabGroups.length, 'tab groups');
        
        tabGroups.forEach((tabGroup, groupIndex) => {
            // Updated selectors for MkDocs Material tabs
            const inputs = tabGroup.querySelectorAll('input[type="radio"]');
            const labels = tabGroup.querySelectorAll('label');
            
            console.log(`[Platform Tabs] Group ${groupIndex}: ${inputs.length} tabs`);
            
            // Debug: log the actual structure
            if (inputs.length === 0) {
                console.log(`[Platform Tabs] Group ${groupIndex} HTML:`, tabGroup.innerHTML.substring(0, 200));
            }
            
            // Find the right tab to select
            let targetInput = null;
            
            inputs.forEach((input, index) => {
                const label = labels[index];
                if (!label) return;
                
                const labelText = label.textContent.trim().toLowerCase();
                console.log(`  Tab ${index}: "${labelText}"`);
                
                if (targetPlatform === 'windows' && labelText === 'windows') {
                    targetInput = input;
                } else if (targetPlatform === 'unix' && 
                          (labelText === 'macos/linux' || labelText === 'macos' || labelText === 'linux')) {
                    // For unix, prefer combined tab, then macOS
                    if (labelText === 'macos/linux' || (!targetInput && labelText === 'macos')) {
                        targetInput = input;
                    }
                }
            });
            
            // Select the tab by clicking it (more reliable than setting checked)
            if (targetInput) {
                console.log(`[Platform Tabs] Clicking tab for ${targetPlatform}`);
                targetInput.click();
            }
        });
        
        // Reset flag after a short delay
        setTimeout(() => {
            isAutoSelecting = false;
        }, 500);
    }
    
    // Save user's manual selection
    function saveUserPreference(event) {
        // Don't save if this is an auto-selection
        if (isAutoSelecting) return;
        
        if (!event.target.matches('.tabbed-set input[type="radio"]')) return;
        
        const label = event.target.nextElementSibling;
        if (!label) return;
        
        const labelText = label.textContent.trim().toLowerCase();
        console.log('[Platform Tabs] User manually selected:', labelText);
        
        if (labelText === 'windows') {
            localStorage.setItem('preferredPlatform', 'windows');
        } else if (labelText === 'macos/linux' || labelText === 'macos' || labelText === 'linux') {
            localStorage.setItem('preferredPlatform', 'unix');
        }
    }
    
    // Initialize after a short delay to ensure tabs are rendered
    setTimeout(() => {
        console.log('[Platform Tabs] Running platform detection...');
        selectPlatformTabs();
    }, 200);
    
    // Listen for manual tab selections
    document.addEventListener('change', saveUserPreference);
});
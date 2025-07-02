// Auto-center the current section in the progress tracker
document.addEventListener('DOMContentLoaded', function() {
    const progressTrackers = document.querySelectorAll('.progress-tracker');
    
    progressTrackers.forEach(tracker => {
        const currentElement = tracker.querySelector('.current');
        if (currentElement) {
            // Use requestAnimationFrame to ensure DOM is fully rendered
            requestAnimationFrame(() => {
                // Calculate scroll position to center the current element
                const trackerWidth = tracker.offsetWidth;
                const currentLeft = currentElement.offsetLeft;
                const currentWidth = currentElement.offsetWidth;
                const scrollPosition = currentLeft + (currentWidth / 2) - (trackerWidth / 2);
                
                // Scroll to center the current element
                tracker.scrollLeft = scrollPosition;
            });
        }
    });
    
    // Also handle window resize
    let resizeTimeout;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(() => {
            progressTrackers.forEach(tracker => {
                const currentElement = tracker.querySelector('.current');
                if (currentElement) {
                    const trackerWidth = tracker.offsetWidth;
                    const currentLeft = currentElement.offsetLeft;
                    const currentWidth = currentElement.offsetWidth;
                    const scrollPosition = currentLeft + (currentWidth / 2) - (trackerWidth / 2);
                    tracker.scrollLeft = scrollPosition;
                }
            });
        }, 100);
    });
});
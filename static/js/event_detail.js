document.addEventListener("DOMContentLoaded", function() {
    const images = document.querySelectorAll('.event-description img');

    images.forEach(img => {
        const maxWidth = 750; // Maximum width in pixels

        // Ensure the image has loaded before accessing its dimensions
        if (img.complete) {
            resizeImage(img, maxWidth);
        } else {
            img.addEventListener('load', () => {
                resizeImage(img, maxWidth);
            });
        }
    });
});

function resizeImage(img, maxWidth) {
    const originalWidth = img.naturalWidth;
    const originalHeight = img.naturalHeight;

    if (originalWidth > maxWidth) {
        const scaleRatio = maxWidth / originalWidth;
        const newWidth = originalWidth * scaleRatio;
        const newHeight = originalHeight * scaleRatio;

        img.style.width = `${newWidth}px`;
        img.style.height = `${newHeight}px`;
    } else {
        // If the image is smaller than the max width, keep its original size
        img.style.width = `${originalWidth}px`;
        img.style.height = `${originalHeight}px`;
    }
}
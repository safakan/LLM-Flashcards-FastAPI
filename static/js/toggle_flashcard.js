function toggleFlashcard() {
    var flashcardContainer = document.querySelector('.flashcard-container');
    var indicator = document.getElementById('flashcardIndicator');
    
    flashcardContainer.classList.toggle('flipped');
    
    if (flashcardContainer.classList.contains('flipped')) {
        indicator.textContent = 'Back';
    } else {
        indicator.textContent = 'Front';
    }
}

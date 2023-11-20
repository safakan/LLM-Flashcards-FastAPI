var popup = document.getElementById('loginPopup');
var close = document.getElementsByClassName("close")[0];
var container = document.querySelector('.container');
var flashcardContainer = document.querySelector('.flashcard-container');

var loginButton = document.getElementById('loginButton');
if (loginButton) {
    loginButton.onclick = function() {
        popup.style.display = "block";
        container.classList.add('popup-active');
        flashcardContainer.classList.add('popup-active');
    };
}

close.onclick = function() {
    popup.style.display = "none";
    container.classList.remove('popup-active');
    flashcardContainer.classList.remove('popup-active');
};

window.onclick = function(event) {
    if (event.target == popup) {
        popup.style.display = "none";
        container.classList.remove('popup-active');
        flashcardContainer.classList.remove('popup-active');
    }
};

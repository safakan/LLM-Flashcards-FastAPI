document.addEventListener('DOMContentLoaded', function() {
    var userInput = document.getElementById('userInput');
    userInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            createDeckAndDisplayFirstCard(this.value);
        }
    });
});

function createDeckAndDisplayFirstCard(promptText) {
    fetch('/create_deck_from_input', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ prompt: promptText })
    })
    .then(response => response.json())
    .then(data => {
        if (data && data.first_card) {
            updateCardDisplay(data.first_card);
        }
    })
    .catch(error => console.error('Error:', error));
}

function updateCardDisplay(card) {
    if (card) {
        document.getElementById('cardFront').textContent = card.front;
        document.getElementById('cardBack').textContent = card.back;
    } else {
        // Handle the scenario when there's no card data.
        document.getElementById('cardFront').textContent = 'No cards available';
        document.getElementById('cardBack').textContent = '';
    }
}

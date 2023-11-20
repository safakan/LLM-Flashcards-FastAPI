document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.menu-button.browse-decks').addEventListener('click', function() {
        fetch('/api/decks')
            .then(response => response.json())
            .then(data => {
                const deckList = document.getElementById('deckList').querySelector('tbody');
                deckList.innerHTML = ''; // Clear existing rows
                data.forEach(deck => {
                    const row = deckList.insertRow();
                    row.innerHTML = `<td>${deck.id}</td><td>${deck.name}</td>`;
                    row.addEventListener('click', () => {
                        // Handle the click event for each deck
                        console.log(`Deck clicked: ${deck.id}`);
                        // Implement your logic here, e.g., redirecting to another page
                    });
                });
                document.getElementById('deckListingSection').style.display = 'block';
            })
            .catch(error => console.error('Error:', error));
    });
});

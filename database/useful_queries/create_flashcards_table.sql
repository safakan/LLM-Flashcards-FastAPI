CREATE TABLE IF NOT EXISTS flashcards (
    id INTEGER PRIMARY KEY,
    deck_id INTEGER,
    front TEXT NOT NULL,
    back TEXT NOT NULL,
    FOREIGN KEY (deck_id) REFERENCES decks(id)
);
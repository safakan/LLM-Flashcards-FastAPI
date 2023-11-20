import sqlite3
import pandas as pd
import os
import glob

"""
This one captures all the csv files in the directory and processes them to populate the database.
CSVs are for decks. there're 3 columns: front, back, deck_name

decks table is populated with the deck_name
flashcards table is populated with front & back values of flashcards linked with deck_id
"""


def insert_deck(cursor, deck_name):
    cursor.execute("INSERT INTO decks (name) VALUES (?)", (deck_name,))
    return cursor.lastrowid  # Assuming 'id' is auto-incremented

def insert_flashcard(cursor, deck_id, front, back):
    cursor.execute("INSERT INTO flashcards (deck_id, front, back) VALUES (?, ?, ?)", (deck_id, front, back))

def populate_database(csv_file, connection):
    df = pd.read_csv(csv_file)
    unique_deck_names = df['deck_name'].unique()

    for deck_name in unique_deck_names:
        cursor = connection.cursor()

        # Insert deck and get its ID
        deck_id = insert_deck(cursor, deck_name)

        # Filter rows for the current deck
        deck_rows = df[df['deck_name'] == deck_name]

        for _, row in deck_rows.iterrows():
            insert_flashcard(cursor, deck_id, row['front'], row['back'])
        
        connection.commit()

def process_all_csv_files(connection):
    csv_files = glob.glob('*.csv')
    for csv_file in csv_files:
        print(f"Processing {csv_file}...")
        populate_database(csv_file, connection)

def main():
    # Adjust the path to point to the 'test.db' in the root directory
    db_path = os.path.join(os.path.dirname(__file__), '..', '..', 'test.db')
    connection = sqlite3.connect(db_path)

    process_all_csv_files(connection)

    connection.close()


if __name__ == "__main__":
    main()

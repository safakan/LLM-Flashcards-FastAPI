import sqlite3
import os

def delete_duplicates(connection):
    cursor = connection.cursor()

    # Query to find duplicate deck names (except the one with the lowest id)
    find_duplicates_query = """
    SELECT id FROM decks
    WHERE name IN (
        SELECT name FROM decks
        GROUP BY name
        HAVING COUNT(name) > 1
    )
    AND id NOT IN (
        SELECT MIN(id) FROM decks
        GROUP BY name
        HAVING COUNT(name) > 1
    )
    """
    
    cursor.execute(find_duplicates_query)
    duplicate_ids = [row[0] for row in cursor.fetchall()]

    if duplicate_ids:
        # Query to delete associated flashcards
        delete_flashcards_query = "DELETE FROM flashcards WHERE deck_id IN ({})".format(','.join('?' for _ in duplicate_ids))
        cursor.execute(delete_flashcards_query, duplicate_ids)

        # Query to delete duplicate decks
        delete_decks_query = "DELETE FROM decks WHERE id IN ({})".format(','.join('?' for _ in duplicate_ids))
        cursor.execute(delete_decks_query, duplicate_ids)

        connection.commit()
        print(f"Deleted duplicates and associated flashcards for deck IDs: {duplicate_ids}")
    else:
        print("No duplicates found.")

def main():
    db_path = os.path.join(os.path.dirname(__file__), '..', '..', 'test.db')
    connection = sqlite3.connect(db_path)

    try:
        delete_duplicates(connection)
    finally:
        connection.close()

if __name__ == "__main__":
    main()

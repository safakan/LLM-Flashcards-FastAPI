- LLM logic

What Happens During User Login:
The user enters their credentials into the frontend form.
JavaScript (AJAX) captures these credentials and sends a POST request to the /login route.
The /login route verifies the credentials against the database.
If the credentials are correct, the user is logged in, and a session/cookie is set.
Basic yet complete user authentication flow.















------- active deck fix
The persistent presence of the deck across page reloads or sessions might be due to the way the ActiveDeck singleton is implemented in your application. The singleton pattern ensures that only one instance of a class exists during the application's lifecycle. In a server environment like FastAPI, this can mean the ActiveDeck instance remains active and retains its state as long as the server is running.

To manage this and control when the deck should be available, you could consider the following approaches:

Session-Based Deck Management: Instead of using a singleton pattern for the deck, you could store deck information in user sessions. This way, each user would have their own deck that persists only for their session.

Reset Deck on Logout/Login: Provide functionality to reset or clear the ActiveDeck instance when a user logs out, or when a new session starts. This would ensure that a new user starting a session does not see a previous user's deck.

Database Storage: Store deck information in a database linked to a user account. Whenever a user logs in, their deck is loaded from the database. This approach is more complex but allows for persistent, user-specific decks that can be accessed across different sessions and devices.

Expire the Deck After Inactivity: Implement a timeout feature where the deck resets after a certain period of inactivity.

Manual Reset Option: Provide a button or option in the UI for users to manually reset or clear the deck.

Each of these approaches has its considerations regarding user experience and application complexity. The choice largely depends on how you want the decks to behave in relation to user sessions and interactions.
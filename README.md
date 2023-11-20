# LLM FLASHCARDS APP 
This prototype app aims revolutionize flashcard learning by enabling users to generate custom flashcard decks for an enhanced and personalized practice experience. Break free from conventional flashcard usage and unleash your creativity with our innovative approach.

The app is designed with a front-end agnostic architecture, utilizing FastAPI for robust backend performance. It leverages Langchain for efficient LLM chaining, complemented by streamlined vanilla HTML/JS/CSS for the front-end.

Front-end agnostic FastAPI app benefiting from Langchain for LLM chains and vanilla HTML/JS/CSS for front-end.

**Readme Contents**
- 1.0 Stack
- 1.1 Installation
- 1.2 Usage
- 1.3 Understanding the Codebase

## 1.0 Stack
- Python, SQL, Javascript, HTML, CSS
- FastAPI, langchain, uvicorn, fastapi, passlib, Jinja2, python-multipart, python-dotenv, openai, bcrypt

## 1.1 Installation
1. Clone the repository: `git clone https://github.com/Safakan/LLM-Flashcards-FastAPI.git` or via the GitHub Desktop app.
2. Install the required dependencies: `pip install -r requirements.txt` (ideally in a virtual environment)

OR
1. Create a docker container using the Dockerfile.


## 1.2 Usage
1. Ensure you are in the root directory and have a .env file with your "OPENAI_API_KEY" set to your private key.
 - Confirm that the API key is correctly set in the environment.
2. Run the application: `uvicorn main:app --reload`
3. Wait for the application to run on your browser.
4. Register/Login to use.
5. Give AI a prompt to generate you a deck of cards.
 - AI is accustomed to generate you a deck of cards, just give it a context and tell what you want.



## 1.3 Understanding the Codebase
The application is primarily driven by main.py located in the root directory. The diagram below illustrates the repository's sub-directory structure. The modularized codebase is designed for clarity and ease of navigation. For a detailed understanding, please refer to the descriptions of each section below.

![Codebase](docs/images/understanding_codebase.png)

### Root Directory (APP)
The root directory contains essential files for the application's operation:
- `main.py`: The entry point of the application. It performs several critical functions:
  - Initializes and loads environment variables.
  - Prepares the database schema before the application starts serving requests.
  - Incorporates all routes and endpoints from `routes/web.py`.
  - Mounts a directory to serve static files.
- `readme.md`: Provides an overview and documentation for the project.
- `requirements.txt`: Lists all the Python dependencies.
- `test.db`: A sample database file used for testing.
- `LICENSE`: The license file for the project.
- Various configuration files for Git and Docker.


### Templates Directory
- Contains HTML templates used by the application, such as `index.html`.

### Static Directory
- Manages static assets, divided into two sub-directories:
  - `js/`: Contains independent JavaScript modules.
  - `styles/`: Houses CSS modules for styling.

### Routes Directory
- Central location for handling API endpoints:
  - `web.py`: Sets up the router with all endpoints and integrates Jinja templates.


### Database Directory
- Manages database interactions and models:
  - `models.py`: Defines data models.
  - `database.py`: Handles the database connection.
  - `query_database.py`: A Database Query CLI Tool for querying the database.
    - Usage: `python .\query_database.py --query "Select * from users"`
    - Or: `python .\query_database.py --file .\query.sql`

### Auth Directory
- `authentication.py`: Manages user authentication, including password hashing and verification.

### Chains Directory
- `create_deck_from_input.py`: Utilizes LLM chains to generate flashcard decks from text inputs, converting them into a JSON format for processing.

### Objects Directory
- Stores abstract objects with complex utilities for the application:
  - Currently includes `active_deck.py`.

### Docs Directory
- A dedicated space for all documentation-related materials.
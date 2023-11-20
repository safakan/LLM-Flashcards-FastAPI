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
The app runs from the single file main.py in the root directory, the rest in the diagram below are sub-directories of the repository. Modularized codebase aims to provide clear links within the application.
![Codebase](docs/images/understanding_codebase.png)

### main.py
- Runs the app itself.
- - The environment variables are loaded.
- - Ensures the database schema is prepared before the application starts serving requests.
- - Adds all the routes and endpoints defined in routes(web.py) to the main application.
- - Mounts a directory to serve static files in a FastAPI application

### templates
- has the template html files

### static
- has the static files to be served

routes/web.py
- has the router set up and the jinja templates
- all routes are defined here

database/models.py
- contains all the data models

database/database.py
- connection to the database

auth/authentication.py
- handles password and user verification / hashing
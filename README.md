# LLM FLASHCARDS APP 
- An app to generate custom flashcard decks and practice. Challenge your creativity to stir away from mainstream way of using flashcards.
- Front-end agnostic FastAPI app benefiting from Langchain for LLM chains and vanilla HTML/JS/CSS for front-end.

**Readme Contents**
- 1.0 Stack
- 1.1 Installation
- 1.2 Usage
- 1.3 Understanding the Codebase

## 1.0 Stack
- Python, SQL, Javascript, HTML, CSS
- FastAPI, langchain, uvicorn, fastapi, passlib, Jinja2, python-multipart, python-dotenv, openai, bcrypt

## 1.1 Installation
1. Clone the repository: `git clone https://github.com/Safakan/TalkWithYourFiles.git` or by using the GitHub Desktop app.
2. Install the required dependencies: `pip install -r requirements.txt` (ideally in a virtual environment)

OR
1. Create a docker container using the Dockerfile.


## 1.2 Usage
1. Make sure you're in the root directory and have a .env file with your "OPENAI_API_KEY" set to your private key.
 - just make sure the api key is set in the environment.
2. Run the application: `uvicorn main:app --reload`
3. Wait for the application to run on your browser.
4. Register/Login to use.
5. Give AI a prompt to generate you a deck of cards.
 - AI is accustomed to generate you a deck of cards, just give it a context and tell what you want.



## 1.3 Understanding the Codebase
![Codebase](docs/images/understanding_codebase.png)

main.py
- runs the app

templates
- has the template html files

static
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
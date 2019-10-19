# README

Ga Tech CS-6460 Project - Game based introductory computer science course (snappy name TBD).

## Running the application

1. Setup the environment
    ```Bash
    make
    ```
2. Set the JS and CSS watcher
    ```Bash
    make watch
    ```
3. Start the server
    ```
    make start
    ```
4. Navigate to http:/localhost:8000/game/index/ (basic Hello World application)

## Installing a JS library

1. Install the package
    ```Bash
    npm install --save-dev <package>
    ```
2. Commit the updated `package-lock.json` file.

## Installing a Python library

1. Add the library to `requirements.txt`
2. Run 
    ```Bash
    make venv
    ```

## Application structure

- `api/`: Django app for the backend API - will contain the database models and API endpoints
- `front/`: Django app for the front end - will contain HTML templates and AJAX views
- `static/`: Directory containing javascript, scss, and css files. 

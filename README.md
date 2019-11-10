# README

Ga Tech CS-6460 Project. This application is an online, game based, introductory computer science (CS1) course 
which leverages the Blockly programming framework to deliver content. 

## Running the application

The application itself runs inside of a docker container. See the `Makefile` for detailed commands
on building / running the container. 

Command                   | Run in the shell? | Description
--------------------------|-------------------|-----------------
`make build`              | No                | Builds the container
`make start`              | No                | Starts the django server
`make shell`              | No                | Opens a shell inside the docker container (to be used to run installation / db config commands)
`make make_migration`     | No                | Creates new migrations
`make migrate`            | Yes               | Runs the database migrations
`make build_game_configs` | Yes               | Loads static content into the DB
 

## Installing a JS library

1. Connect to the docker shell
	```Bash
	make shell
	```
2. Install the package
	```Bash
	npm install --save-dev <package>
	```
2. Commit the updated `package-lock.json` file.

## Installing a Python library

1. Connect to the docker shell
	```Bash
	make shell
	```
1. Add the library to `requirements.txt`
2. Run 
    ```Bash
    make python_install
    ```

## Application structure

- `account/`: Django app for login and registration.
- `api/`: Django app for the backend API - will contain the database models and API endpoints
- `front/`: Django app for the front end - will the user facing and AJAX views
- `static/`: Directory containing javascript, scss, and css files. 
- `templates/`: Directory containing html templates

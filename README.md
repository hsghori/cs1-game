# README

Ga Tech CS-6460 Project. This application is an online, game based, introductory computer
science (CS1) course which leverages the Blockly programming framework to deliver content.

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


 ## To launch the application locally:

 You will need to have three terminal applications open to run this program locally. You
 should also have Docker installed. Each terminal should start in the project root.

 In terminal 1 run:
 - `make build` - builds the Docker image
 - `make start` - starts the Docker container and launches the server

In terminal 2 run:
- `make shell` - connects to a bash shell in the running Docker container
- `make` - Installs all dependencies

In terminal 3 run: (only required if you plan to change JS or SCSS files)
- `npm install` - install all required npm packages
- `make watch` - sets up a watcher job for changes to JS or SCSS

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

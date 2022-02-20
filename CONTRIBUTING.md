# Contributing

## Development Environment Setup

Install docker, docker-compose, python, and npm. Stick to the python version used in the Dockerfile.

### Database

Start a local MySQL database with Docker.

```shell
cd data
docker-compose up -d
```

### Flask API

Create a virtual environment and install the dependencies.

```shell
cd api
python -m venv venv
pip install -e .
```

Set variables with bash.

```bash
export FLASK_APP=whatsin
export FLASK_ENV=development
```

Set variables with PowerShell.

```PowerShell
$env:FLASK_APP='whatsin'
$env:FLASK_ENV='development'
```

Start the Flask development server.

```shell
python -m flask run
```

### React App

Set the environment variable for the API base API URI.

```PowerShell
$env:REACT_APP_API_BASE_URI="http://127.0.0.1:5000/whatsin"
```

Install the project requirements and start the development server.

```shell
cd web
npm install
npm start
```

This runs the app in the development mode. Open [http://localhost:3001](http://localhost:3001) to view it in the browser.

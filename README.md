# What's In?

'Whats In?' allows you to quickly find out what ingredients are commonly included in a recipe so you don't have to trawl through recipe websites for ingredient ideas and suggestions.

## Development Environment

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

## Build

Build the Docker image for `whatsin-api`.

```shell
docker build --no-cache -t tomelvidge/whatsin-api:latest -t tomelvidge/whatsin-api:{version} api
```

Once built the entire backend can be run locally with docker-compose.

```shell
docker-compose up -d
```

## Deployment

Create a release in GitHub to trigger an action which builds and publishes the whatsin-api Docker image.

The frontend is automatically deployed by Netlify on commits to master. Make sure to update the environment variable for the API base API URI in Netflify.

The backend (api and database) containers can be deployed anywhere. For the simplest deployment clone this repo and use `docker-compose.yml`.

## Troubleshooting

Make sure the config from environment variables has been added to `config.py` on `whatsin-api` container start.

```shell
docker exec -it whatsin-api-1 /bin/bash
```

```shell
cd /app/instance
cat config.py
```
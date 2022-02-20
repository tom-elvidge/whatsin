# Deployment

Create a release in GitHub to trigger an action which builds and publishes the whatsin-api Docker image.

The frontend is automatically deployed by Netlify on commits to master. Make sure to update the environment variable for the API base API URI in Netflify.

The backend (api and database) containers can be deployed anywhere. For the simplest deployment clone this repo and use `docker-compose.yml`.
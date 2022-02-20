# Troubleshooting

## Dockerfile

### Builds

You may have to build the `whatsin-api` container locally to troubleshoot and test changes.

```shell
docker build --no-cache -t whatsin-api:latest api
```

Once built the entire backend can be run locally with docker-compose. Will have to make changes to the image to use the image built locally.

```shell
docker-compose up -d
```

### Environment Variables

Make sure the config from environment variables has been added to `config.py` on `whatsin-api` container start.

```shell
docker exec -it whatsin-api-1 /bin/bash
```

```shell
cd /app/instance
cat config.py
```

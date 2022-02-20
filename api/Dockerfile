FROM python:3.9.10-slim-buster

# Environment variable defaults
ENV MYSQL_HOST="0.0.0.0"
ENV MYSQL_PORT=3306
ENV MYSQL_USER="root"
ENV MYSQL_PASSWORD="password"
ENV MYSQL_DATABASE="WhatsIn"

COPY . /app
WORKDIR /app

RUN chmod +x /app/start.sh

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --force -r requirements.txt

EXPOSE 8080/tcp

ENTRYPOINT [ "/bin/bash", "/app/start.sh" ]
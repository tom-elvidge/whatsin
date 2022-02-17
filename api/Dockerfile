FROM python:3.9

ENV MYSQL_HOST="localhost"
ENV MYSQL_PORT=3306
ENV MYSQL_USER="root"
ENV MYSQL_PASSWORD="password"
ENV MYSQL_DATABASE="WhatsIn"

# python latest
# upgrade, update, apt, pip

COPY . /api

RUN pip install wheel
RUN python /api/setup.py bdist_wheel
# Todo: Handle different versions
RUN pip install /api/dist/whatsin-1.0.0-py3-none-any.whl
RUN export FLASK_APP=whatsin

RUN pip install waitress

EXPOSE 8080/tcp
EXPOSE 8080/udp

RUN chmod +x /api/start.sh

CMD ["/bin/bash", "/api/start.sh"]
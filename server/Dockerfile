FROM python:3.10-alpine
ENV FLASK_DEBUG="off"
ENV FLASK_APP=app.py
ENV PORT=5000

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["/bin/sh", "start.sh"]

# syntax=docker/dockerfile:1
FROM python:3.9.10-slim-bullseye

# provide credentials to firestore
ENV GOOGLE_APPLICATION_CREDENTIALS=/usr/src/app/secret/firestore-credentials.json
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONPATH=/usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt /tmp/requirements.txt

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    python3 -m venv $VIRTUAL_ENV && \
    pip install -U --no-cache-dir pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt

COPY app/ .

EXPOSE 5000

CMD ["gunicorn", "wsgi:app"]

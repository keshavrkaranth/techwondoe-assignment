FROM python:3.8-slim-buster


# setting work directory
WORKDIR /usr/src/app


# env variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWEITEBYTECODE 1


# install psycopg dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*


# install dependencies
COPY requriments.txt ./requriments.txt
RUN pip install -r requriments.txt


COPY . .



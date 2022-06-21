FROM python:latest
WORKDIR /code
COPY . .
RUN "pip install -r requirements.txt"
ENTRYPOINT "python pie.py" && /bin/bash
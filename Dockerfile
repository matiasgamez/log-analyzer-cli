FROM python:3.11

WORKDIR /app

COPY . .

ENTRYPOINT ["python","src/main.py"]



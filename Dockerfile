# 
FROM python:3.11.9-slim-bullseye

# 
WORKDIR /app

# 

COPY . .

RUN pip install -r requirements.txt


EXPOSE 80
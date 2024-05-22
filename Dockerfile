# 
FROM python:latest

# 
WORKDIR /app

# 
COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 8001
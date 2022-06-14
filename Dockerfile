FROM python:3.8-buster

WORKDIR /prova_api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8081

CMD ["python", "prova_api.py"]

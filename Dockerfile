FROM python:3.8-buster

WORKDIR /TP1-2DOCKER

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY prova_api.py .

EXPOSE 5000

CMD ["python", "prova_api.py"]
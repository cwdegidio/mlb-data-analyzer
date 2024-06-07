FROM python:3.12.3-alpine
WORKDIR /mlb-data-analyzer

COPY main.py .
COPY requirements.txt .
COPY ./services ./services
COPY ./utility ./utility
RUN pip install -r requirements.txt

CMD ["python", "./main.py"]

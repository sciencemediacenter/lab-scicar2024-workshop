FROM python:3.11

WORKDIR /workspace

COPY . .

RUN pip install --upgrade pip

RUN apt-get update

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/workspace/src \
    DATA_LOCATION=/workspace/data
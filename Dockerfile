FROM python:3

RUN mkdir /app

WORKDIR /app

RUN apt-get update
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY main.py tripplite.py /app/

CMD ["python", "main.py"]
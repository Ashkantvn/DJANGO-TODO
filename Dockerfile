FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /todo

COPY requirements.txt /todo/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /todo/

CMD [ "python",'manage.py','runserver',"0.0.0.0:8080" ]
FROM python:3

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000
CMD [ "python", "-m", "flask", "run", "-h", "0.0.0.0"]
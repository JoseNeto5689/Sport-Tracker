FROM python:3.12

WORKDIR /app

RUN pip3 install flask

RUN pip3 install typing

RUN pip3 install flask-cors

COPY . .

CMD [ "python3", "src/main.py"]

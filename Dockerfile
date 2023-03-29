FROM python:3.9.4

EXPOSE 8080

WORKDIR /data_app

RUN apt-get update

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app.py", "--server.port", "8080","--server.enableCORS", "false"]

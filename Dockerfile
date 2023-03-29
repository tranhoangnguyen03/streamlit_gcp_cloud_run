FROM python:3.9.4

EXPOSE 8080

RUN apt-get update

COPY . ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /data_app

CMD ["streamlit", "run", "app.py", "--server.port", "8080","--server.enableCORS", "false"]

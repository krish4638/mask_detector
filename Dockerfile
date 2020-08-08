FROM python:3.7-slim-buster
RUN pip3 install --upgrade pip
RUN pip3 install flask flask_cors opencv-python 
RUN pip3 install tensorflow
RUN apt-get -y update
RUN apt-get install -y libgtk2.0-dev
RUN mkdir app
COPY . /app
EXPOSE 8081
WORKDIR /app
ENTRYPOINT ["python3", "app.py"]
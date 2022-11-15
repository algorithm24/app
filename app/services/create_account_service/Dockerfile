FROM python:3.9-alpine
RUN apk update expat=2.5.0
RUN apk upgrade expat
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 4000
CMD [ "python3", "app.py"]

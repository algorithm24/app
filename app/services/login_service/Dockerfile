#  High severity vulnerability found in expat/expat
#   Description: Use After Free
#   Info: https://security.snyk.io/vuln/SNYK-ALPINE316-EXPAT-3062883
#   Introduced through: expat/expat@2.4.9-r0, .python-rundeps@20221025.034103
#   From: expat/expat@2.4.9-r0
#   From: .python-rundeps@20221025.034103 > expat/expat@2.4.9-r0
#   Fixed in: 2.5.0-r0
FROM python:3.9-alpine
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8000
CMD [ "python3", "app.py"]
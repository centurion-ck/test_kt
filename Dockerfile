FROM python:3.11-slim

RUN apt-get update && apt-get install -y wget unzip

RUN wget https://releases.hashicorp.com/terraform/1.8.5/terraform_1.8.5_linux_amd64.zip

RUN unzip terraform_1.8.5_linux_amd64.zip

RUN mv terraform /usr/local/bin/

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python","app.py"]
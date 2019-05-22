FROM python:3.5

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src /home

WORKDIR /home

CMD ["bash", "-c",  "python", "rancherbot-telegram.py"]

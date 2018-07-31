FROM python:3.6-slim

ENV HOME=/app

WORKDIR $HOME

COPY requirements.txt $HOME/

RUN pip install -r requirements.txt

COPY . $HOME/

CMD ["ddtrace-run", "python3", "main.py"]

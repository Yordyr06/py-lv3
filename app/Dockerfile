FROM python:3.8

WORKDIR /app
COPY requirement.txt /app/requirement.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirement.txt

COPY . /app

CMD bash -c "while true; do sleep 1; done"
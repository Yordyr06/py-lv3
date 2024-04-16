FROM python:3.10

WORKDIR /app
COPY requirement.txt /app/requirement.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirement.txt

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
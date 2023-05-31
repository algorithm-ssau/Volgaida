FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "api", "--port", "8000"]

#CMD gunicorn main:app --workers 3 --worker-class uvicorn.workers.UvicornWorker --bind=api:8000

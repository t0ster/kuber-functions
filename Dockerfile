FROM python:3-slim

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY . /app
WORKDIR /app
CMD ["gunicorn", "--threads", "3", "--bind", ":5000", "--access-logfile", "-", "--error-logfile", "-", "wsgi:app"]

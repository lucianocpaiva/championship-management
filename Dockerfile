FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app/

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY docker/entrypoint.sh /tmp/

RUN chmod u+x /tmp/entrypoint.sh

ENTRYPOINT [ "/tmp/entrypoint.sh" ]
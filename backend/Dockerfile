FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
	postgresql-client \
    && rm -rf /var/lib/apt/lists/*
	
COPY ./app ./

RUN chmod +x /app/requirements.txt
RUN chmod +x /app/entrypoint.sh

RUN pip install --no-cache-dir -r requirements.txt

CMD ["/app/entrypoint.sh"]
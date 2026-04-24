#!/bin/sh

set -e

echo "Check postgres ready ${POSTGRES_HOST}:${POSTGRES_PORT}..."

until pg_isready -h ${POSTGRES_HOST} -p ${POSTGRES_PORT} -U ${POSTGRES_USER} -d ${POSTGRES_DB}; do
  echo "Postgres is unavailable, retry..."
  sleep 2
done

echo "Postgres is available"

echo "Start migration"

python src/manage.py migrate

echo "Migration completed successfully"

echo "Collect base static"

python src/manage.py collectstatic --clear --noinput

echo "Collect base static completed successfully"

echo "Start django backend"

python src/manage.py runserver 0.0.0.0:${BACKEND_PORT}
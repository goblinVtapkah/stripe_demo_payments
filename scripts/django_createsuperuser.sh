#!/bin/bash

set -e

echo "Start create superuser in database"

docker compose exec backend python src/manage.py createsuperuser

echo "Create superuser completed successfully"
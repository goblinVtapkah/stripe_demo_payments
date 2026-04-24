#!/bin/bash

set -e

echo "Start migration"

docker compose exec backend python src/manage.py migrate

echo "Migration completed successfully"
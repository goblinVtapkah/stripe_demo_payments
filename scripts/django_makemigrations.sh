#!/bin/bash

set -e

echo "Start makemigrations"

docker compose exec backend python src/manage.py makemigrations

echo "Makemigrations completed successfully"
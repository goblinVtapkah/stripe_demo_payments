#!/bin/bash

set -e

echo "Collect base static"

docker compose exec backend python src/manage.py collectstatic

echo "Collect base static completed successfully"
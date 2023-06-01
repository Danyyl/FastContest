#!/bin/bash

cd src

if [[ "${1}" == "celery" ]]; then
  echo "===== Celery mode ====="
  celery --app=test.tasks:celery worker --loglevel=DEBUG
elif [[ "${1}" == "flower" ]]; then
  echo "===== Flower mode ====="
  celery --app=test.tasks:celery flower
fi

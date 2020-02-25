#!/bin/bash

cd /app/zen

gunicorn app:app --bind 0.0.0.0:8888 -w 4 --reload --access-logfile -
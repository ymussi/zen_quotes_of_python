#!/bin/bash

cd /app/zen

gunicorn run:app --bind 0.0.0.0:5000 -w 4 --reload --access-logfile -
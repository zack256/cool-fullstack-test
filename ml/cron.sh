#!/bin/bash

export $(grep -v '^#' /app/ml.env | xargs)

/venv/bin/python /app/app.py
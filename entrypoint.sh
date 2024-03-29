#!/bin/bash

set -e

echo "${0}: running migrations."
python manage.py makemigrations --merge
python manage.py migrate --noinput

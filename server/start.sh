#!/usr/bin/env sh

# migrate database
flask db upgrade
# run main application
python app.py

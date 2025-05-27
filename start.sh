#!/usr/bin/env bash
# start the gunicorn server
gunicorn --config gunicorn.conf.py main:app
#!/usr/bin/env bash
# exit on error
set -o errexit
pip install -r requirements.txt
python -m nltk.downloader punkt # Si usas nltk
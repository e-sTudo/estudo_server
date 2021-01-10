#!/bin/bash
cd "$(dirname "$0")"
export FLASK_APP=serverFlask.py
flask run

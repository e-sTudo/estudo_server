#!/bin/bash
cd "$(dirname "$0")"
export FLASK_APP=server.py
flask run

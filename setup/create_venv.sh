#!/bin/bash

virtualenv venv
source venv/bin/activate

pip3 install --upgrade pip --no-cache-dir
pip3 install -r requirements.txt --no-cache-dir
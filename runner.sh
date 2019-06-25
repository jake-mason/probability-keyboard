#!/bin/bash

if ! [[ -f assets/words ]]; then
	cd assets && sh fetch-assets.sh && cd ..

if ! [[ -d setup/venv ]]; then
	cd setup && sh create_venv.sh && cd ..
fi

source setup/venv/bin/activate

cd src

python3 app.py
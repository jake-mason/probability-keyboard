#!/bin/bash

if ! [[ -d setup/venv ]]; then
	cd setup && sh create_venv.sh && cd ..
fi

source setup/venv/bin/activate

python3 keyboard.py
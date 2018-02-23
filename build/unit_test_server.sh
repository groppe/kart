#!/bin/bash
cd src
pip install coveralls
pip install -r requirements.txt
python -m unittest discover -p "*_test.py"
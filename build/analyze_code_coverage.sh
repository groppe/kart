#!/bin/bash
python -m coverage run -m unittest discover -p "*_test.py"
coveralls
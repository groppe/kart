#!/bin/bash
npm install -g
cd src
pip install -r requirements.txt
sls plugin install -n serverless-python-requirements
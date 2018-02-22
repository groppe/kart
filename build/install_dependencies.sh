#!/bin/bash
npm install
cd ../src
pip install -r requirements.txt
sls plugin install -n serverless-python-requirements
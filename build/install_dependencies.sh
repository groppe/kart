#!/bin/bash
npm install -g serverless
npm install -g serverless-python-requirements
cd src
pip install -r requirements.txt
sls plugin install -n serverless-python-requirements
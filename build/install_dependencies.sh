#!/bin/bash
npm install -g serverless
npm install -g serverless-python-requirements
npm install -g newman
cd src
pip install -r requirements.txt
sls plugin install -n serverless-python-requirements
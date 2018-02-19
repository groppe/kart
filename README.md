[![Build Status](https://travis-ci.org/groppe/kart.svg?branch=development)](https://travis-ci.org/groppe/kart)[![Coverage Status](https://coveralls.io/repos/github/groppe/kart/badge.svg?branch=development)](https://coveralls.io/github/groppe/kart?branch=development)
# Kart
A Slack app and RESTful HTTP API that can be used to keep track of multiplayer game results. It is built using Python, and is deployed to AWS Lambda via Travis CI using the Serverless framework. The application stores player information, game scores, and calculates skill rankings.

## Motivation

Intended for use in any pointed multiplayer game setting, digital or otherwise, where there is not a method of tracking game results and player rankings built in. Originally developed for tracking local Mario Kart game results among a pool of consistent players.

## Getting Started

These instructions will provide assistance in getting the Kart application up and running on a local machine for development purposes. See deployment for notes on how to deploy the application to AWS.

### Prerequisites

The following dependencies are needed to run the application:
 - Python 3.6
 - Node.js 6.11.*
 - MongoDB 3.4.* (a database accessible from the application, not necessarily on the same machine)

The following dependencies are needed to deploy and use the application:
 - AWS account with administrator access
 - Slack account with authorization to add an integration

### Installing

1. Clone or download the entire project.
2. Create the following environment variables (with the appropriate values):
```
MARIO_MONGO_URI: URI to the database that includes credentials with Read/Write permission
MARIO_MONGO_DB: name of the Mongo database to use 
AWS_ACCESS_KEY_ID: Access key with AWS administrator access
AWS_SECRET_ACCESS_KEY: Associated secret key
```
2. Open a bash terminal with administrator privileges and navigate to the root directory of the project.
3. Install the Node dependencies:
```
npm install
```

4. Change working directory to the *src* folder and run the following to install the python dependencies:

```
python -m pip install -r requirements.txt
```

## Deployment

1. Download Python dependencies locally:
```
python -m pip install -r requirements.txt -t .
```
2. Package and deploy to AWS using Serverless (optionally specify deployment stage):
```
sls deploy [--stage dev/test/prod/etc.]
```
3. Add created endpoints to Slack as slash commands, as described [here](https://medium.com/@cu_tech/create-a-slack-slash-command-with-aws-lambda-83fb172f9a74) (start at the "Phew..." section).
## Built With

* [Travis CI](https://travis-ci.org/) - Continuous Integration/Continuous Deployment
* [Serverless](https://serverless.com/) - The deployment framework used
* [MongoDB](https://www.mongodb.com/) - Database
* [NPM](https://www.npmjs.com/) - Node Dependency Management
* [pip](https://pip.pypa.io/en/stable/) - Python Dependency Management
* [numpy](http://www.numpy.org/) - Mathemetical calculations

## Contributing

* Branch off and submit PR's to the `development` branch.
* Work must be fully unit & integration tested.

## Previous Versions

There is currently only a single tagged legacy version, which is a limited iteration of the application that runs on Node.js and only integrates with Slack.

## Authors

* **Joshua Groppe** - *Creator, architect, and lead developer*

## License

This project is licensed under the ISC license.

## Acknowledgments

Coming soon
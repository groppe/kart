[![Build Status](https://travis-ci.org/groppe/mario.svg?branch=development)](https://travis-ci.org/groppe/mario)
# mario
A web application that runs on AWS Lambda for keeping track of your local multiplayer game results. Includes a web interface, documented RESTful API's, and a Slack bot. The application stores player information, game scores, and calculates skill rankings.

## Motivation

Intended for use in any multiplayer game setting where there is not an automated method of tracking game results. Originally developed for tracking local multiplayer Mario Kart game results among a consistent pool of players, which calculated average score rankings and was interfaced using a Slack bot.

## Getting Started

These instructions will provide assistance in getting the mario application up and running on a local machine for development purposes. See deployment for notes on how to deploy the application to AWS.

### Prerequisites

The following are needed to run the application locally:
 - Python 2.7
 - Node.js 6.11.*
 - MongoDB 3.4.* database (on or accessible from the local machine)

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

4. Change working directory to the *server* folder and run the following to install the python dependencies:

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
## Built With

* [Serverless](https://serverless.com/) - The web deployment framework used
* [NPM](https://www.npmjs.com/) - JavaScript Dependency Management
* [pip](https://pip.pypa.io/en/stable/) - Python Dependency Management
* [numpy](http://www.numpy.org/) - Mathemetical calculations
* [MongoDB](https://www.mongodb.com/) - Database

## Contributing

* PR instructions, code review required
* Unit test and integration test standards

## Previous Versions

There is currently only a single tagged legacy version, which is a limited iteration of the application that runs on Node.js and only integrates with Slack.

## Authors

* **Joshua Groppe** - *Creator, architect, and lead developer*

## License

This project is licensed under the ISC license.

## Acknowledgments

Coming soon
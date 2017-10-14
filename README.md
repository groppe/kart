[![Build Status](https://travis-ci.org/groppe/mario.svg?branch=development)](https://travis-ci.org/groppe/mario)
# mario
A web application that runs on AWS Lambda for keeping track of your local multiplayer game results. Includes a web interface, documented RESTful API's, and a Slack bot. The application stores player information, game scores, and calculates skill rankings.

## Motivation

Intended for use in any multiplayer game setting where there is not an automated method of tracking game results. Originally developed for tracking local multiplayer Mario Kart game results among a consistent pool of players, which calculated average score rankings and was interfaced using a Slack bot.

## Getting Started

These instructions will provide assistance in getting the mario application up and running on a local machine for development purposes. See deployment for notes on how to deploy the application to AWS.

### Prerequisites

The following are needed to run the application locally:
```
 - Python 2.7
 - Node.js 6.11.*
 - URI with Read/Write credentials to an existing Mongo database running 3.4.*, which is on or accessible from the local machine.
```

### Installing

1. Clone or download the entire project.
2. Open a bash terminal with administrator privileges and navigate to the root directory of the project.
3. Install the Node dependencies, including the [Serverless](https://serverless.com/) framework:
```
npm install
```

4. Change working directories to the *server* folder and run the following to install the python dependencies:

```
python -m pip install -r requirements.txt -t .
```
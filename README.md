# mario
A web application that runs on AWS Lambda for keeping track of your local multiplayer game results. Includes a web interface, documented RESTful API's, and a Slack bot. The application stores player information, game scores, and calculates skill rankings.

## Motivation

Intended for use in any multiplayer game setting where there is not an automated method of tracking game results. Originally developed for tracking local multiplayer Mario Kart game results among a consistent pool of players, which calculated average score rankings and was interfaced using a Slack bot.

## Getting Started

These instructions will provide assistance in getting the mario application up and running on a local machine for development purposes. See deployment for notes on how to deploy the application to AWS.

### Prerequisites

What is need to run the software locally.
```
Python 2.7
Node.js 6.11.*
URI and Read/Write credentials to an existing Mongo database running 3.4.*, on or accessible from the local machine.
```
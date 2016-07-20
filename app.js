/**
 * A Bot for Slack that tracks Mario Kart results and calculates rankings.
 */

 
 // TOKEN is required for connecting to Slack
if (!process.env.SLACK_TOKEN) {
	console.log('Error: Please specify TOKEN in the environment.');
    process.exit(1);
}

var Botkit = require('botkit');
var controller = Botkit.slackbot();
var bot = controller.spawn({
  token: process.env.SLACK_TOKEN
})

bot.startRTM(function(err,bot,payload) {
  if (err) {
    throw new Error('Could not connect to Slack');
  }
});

controller.hears(["keyword","^pattern$"],["direct_message","direct_mention","mention","ambient"],function(bot,message) {
  // do something to respond to message
  // all of the fields available in a normal Slack message object are available
  // https://api.slack.com/events/message
  console.log("Received message!");
  bot.reply(message,'You used a keyword!');
});
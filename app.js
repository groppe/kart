/**
 * A Bot for Slack that tracks Mario Kart results and calculates rankings.
 */
 
 // SLACK_TOKEN is required for connecting to Slack
if (!process.env.SLACK_TOKEN)
{
	console.log('Error: Please specify SLACK_TOKEN in the environment.');
    process.exit(1);
}
else if (!process.env.MONGODB_URI)
{
	console.log('Error: Please specify MONGODB_URI in the environment.');
    process.exit(1);
}

var Botkit = require('botkit'),
	mongoStorage = require('botkit-storage-mongo')({mongoUri: process.env.MONGODB_URI }),
	controller = Botkit.slackbot({
		storage: mongoStorage
	});

var bot = controller.spawn({
  token: process.env.SLACK_TOKEN
})

bot.startRTM(function(err,bot,payload) {
  if (err) {
    throw new Error('Could not connect to Slack');
  }
});

// users defining what they want to be called
controller.hears(
	['^call me \".*\"$', '^my name is \".*\"$'],
	['direct_mention', 'mention', 'ambient'],
	function(bot, message) {
		console.log(message);

		// extract the name they want to be called
		var title = message.text.split(/[""]/)[1];
		
		// validate it
		if (!title.length || title.length === 0)
		{
			bot.reply(message, 'Sorry, <@' + message.user + '>, that is not a valid title.');
			return;
		}

		// save it
		controller.storage.users.save(
		{
			id: message.user,
			title: title
		},
		function (err) {
			if (err) {
				console.log('There was an error saving the title for ' + message.user);
				console.log(err);
			}
		});

		// reply with the user's new title
		bot.reply(message, 'Alright, <@' + message.user + '>, I will call you ' + title + '!');
});

// users defining what they want to be called
controller.hears(
	['what is my name?', 'what is my title?'],
	['direct_mention', 'mention', 'ambient'],
	function(bot, message) {
		console.log(message);

		// get the user's title from the data base
		controller.storage.users.get(message.user,
		function (err, userData) {

			// if there was an error log it
			if (err) {
				console.log('There was an error retrieving user data for ' + message.user);
				console.log(err);
			}

			// reply with the user's title
			bot.reply(message, '<@' + message.user + '>, your name is ' + userData.title + '!');
		});
});
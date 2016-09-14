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

// dependencies
var Botkit = require('botkit'),
	mongoStorage = require('botkit-storage-mongo')({mongoUri: process.env.MONGODB_URI }),
	controller = Botkit.slackbot({
		storage: mongoStorage
	});

// create the bot
var bot = controller.spawn({
	token: process.env.SLACK_TOKEN
})

// connect to slack
bot.startRTM(function(err,bot,payload) {
	if (err) {
		throw new Error('Could not connect to Slack');
	}
});

// when mario gets invited to a channel
controller.on('channel_joined',
	function(bot, message) {
		console.log(message);

		// reply with mario's excitement
		bot.reply(message, '<!channel>, It\'s a me, Mario!');
	}
);

// when someone suggests a game of kart
controller.hears(
	['(kart)(.*)(\\?)'],
	['direction_mention', 'mention', 'ambient'],
	function(bot, message) {

		// let everyone know
		bot.reply(message, '<!channel>, Let\'s a go!');
	}
);

// TODO: Pick your character

// TODO: Help (list commands & Elo explanation)

// TODO: Game results
controller.hears(
	['^(?:(?:<@\\w+>)\\s(?:[0-9]|[10-12])\\s\\d+)(?:,\\s(?:<@\\w+>)\\s(?:[0-9]|[10-12])\\s\\d+)+$'],
	['direct_mention', 'mention', 'ambient'],
	function(bot, message) {
		console.log(message);
	}
);

// TODO: Rankings

// add character
controller.hears(
	['^add a character$'],
	['direct_mention', 'mention', 'ambient'],
	function(bot, message) {

		askName = function(response, conversation) {

			conversation.on('end', function(conversation) {
				if (conversation.status=='completed') {
					bot.say({
						text: 'I\'m alive!',
						username: conversation.new_character.name,
						channel: message.channel,
						icon_url: conversation.new_character.url
					});
			  	} else {
			    	
			  	}
			});

			conversation.new_character = {};
			conversation.ask('What is this character\'s name?', function(response, conversation) {
				conversation.new_character.name = response.text;
				askImageUrl(response, conversation);
				conversation.next();
			});
		}

		askImageUrl = function(response, conversation) {
			conversation.ask('Alright! What is ' + response.text + '\'s image?', function(response, conversation) {
				conversation.new_character.url = response.text.replace(/[<>]/g, '');
				conversation.say('Ok! ' + conversation.new_character.name + ' has been saved.');


				conversation.next();
			});
		}

		bot.startConversation(message, askName);
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
	}
);

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
			}
		);
	}
);
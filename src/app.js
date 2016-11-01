/**
 * An application tracks Mario Kart results and calculates rankings,
 * and includes a Slack Bot integration.
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
else if (!process.env.DEPLOYMENT_ENVIRONMENT)
{
	console.log('Error: Please specify DEPLOYMENT_ENVIRONMENT in the environment.');
    process.exit(1);
}

// dependencies
const PORT = process.env.PORT || 80;
var express = require("express"),
	bodyParser = require("body-parser"),
	mongodb = require("mongodb"),
	Botkit = require('botkit'),
	requester = require('request'),
	TextTable = require('text-table');

// create the express app
var app = express();

// tell express where to load static (client-side) files from
app.use(express.static(__dirname + "/www"));

// tell express to parse request bodies as json
app.use(bodyParser.json());

// create a database variable outside of the database connection callback 
// to reuse the connection pool.
var db, db_collection_player,
	db_collection_game, db_collection_character;

// connect to the database before starting the application server.
mongodb.MongoClient.connect(process.env.MONGODB_URI, function (err, database) {

	// if there was an error connecting, shutdown the app
	if (err) {
		console.log(err);
		process.exit(1);
	}

	// save database object from the callback for reuse
	db = database;

	console.log("Database connection ready");

	// gather the collections
	db_collection_players = db.collection(process.env.DEPLOYMENT_ENVIRONMENT + '_PLAYER');
	db_collection_games = db.collection(process.env.DEPLOYMENT_ENVIRONMENT + '_GAME');
	db_collection_characters = db.collection(process.env.DEPLOYMENT_ENVIRONMENT + '_CHARACTER');

	// initialize the express app
	var server = app.listen(PORT, function () {
		var port = server.address().port;
    	console.log("App now running on port", port);
	});
});

// GAME RESULTS API ROUTES BELOW

// Generic error handler used by all endpoints
function handleError(res, reason, message, code) {
	console.log("ERROR: " + reason);
	res.status(code || 500).json({"error": message});
}

app.get('/', function (req, res) {
 	res.send('Hello World!');
});

app.post('/', function (req, res) {
	console.log(req);
	res.setHeader('Content-Type', 'application/json');
	var response = {
		response_type: 'in_channel',
    	text: 'It\s-a me, mario!',
	};
 	res.send(JSON.stringify(response));
});

// SLACK BOT INTEGRATION

// create the bot
controller = Botkit.slackbot();
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

// list commands
controller.hears(
	['^help$'],
	['direct_mention'],
	function(bot, message) {

		var text = '*Usage:* @mario <command>\n*Commands:*\n```';
		text += '\n1. add character "<character name>" <character icon url>';
		text += '\n2. characters';
		text += '\n3. my character is "<valid character name>"';
		text += '\n4. my name is "<name you want to be called>"';
		text += '\n5. played <#> games, <user1> <score1>, <user2> <score2>[, <user3> <score3>]';
		text += '\n6. bigboard';
		text += '```';
		bot.reply(message, text);
	}
);

// TODO: Rankings
controller.hears(
	['^bigboard$'],
	['direct_mention'],
	function(bot, message) {
		db_collection_players.find().toArray(function (players_error, players) {
			db_collection_games.find().toArray(function (games_error, games) {
				var board = {};
					
				for (var i = 0; i < players.length; ++i)
				{
					players[i].average_score = 0;
					players[i].games_played = 0;
					players[i].rounds_played = 0;
				}

				for (var i = 0; i < games.length; ++i)
				{
					var game = games[i];

					for (var k = 0; k < game.scores.length; ++k)
					{
						var score = game.scores[k],
							player = players.filter(function (player) { return (player._id === score.player_id) })[0];

						player.games_played += parseInt(game.games);
						player.average_score += score.average;
						player.rounds_played++;
					}
				}

				// sort by average score
				players.sort(function (a, b) { return (b.average_score / b.rounds_played) - (a.average_score / a.rounds_played) });

				var text = '*BOARD*\n';
				var table = [[ 'Rank', 'Name', 'Average', 'Character']];

				for (var i = 0; i < players.length; ++i)
				{
					var player = players[i];
					table.push([ (i + 1).toString(), player.name, (player.average_score / player.rounds_played).toFixed(2), player.character]);
				}

				var text_table = TextTable(table, { align: [ 'l', 'c', 'c', 'c' ] });
				bot.reply(message, text + text_table);
			});
		});
	}
);

// add character
controller.hears(
	['^(add character\\s)(\".*\"\\s)([^\\s]+)$'],
	['direct_mention'],
	function(bot, message) {

		// extract the character information
		var components = message.text.split(/[""]/);

		// make sure its basically in the right format
		if (components.length != 3)
		{
			bot.reply(message, 'Sorry, <@' + message.user + '>, that wasn\'t formatted right.');
			return;
		}

		db_collection_characters.insert({ name: components[1], image: components[2].replace(/[<> ]/g, '') }, function(error, result) {
			if (error)
			{
				bot.reply(message, 'Sorry, <@' + message.user + '>, I wasn\'t able to save that character.');
				return;
			}
			else
			{
				bot.say({text: 'Ok! ' + components[1] + ' has been saved.', channel: message.channel });
				bot.say({
					text: 'I\'m alive!',
					username: components[1],
					channel: message.channel,
					icon_url: components[2].replace(/[<> ]/g, '')
				});
			}
		});
	}
);

// list characters
controller.hears(
	['^characters$'],
	['direct_mention'],
	function(bot, message) {
		db_collection_characters.find().sort({ name: 1 }).toArray(function (error, result) {
			if (error)
			{
				bot.reply(message, 'Sorry, <@' + message.user + '>, I wasn\'t able to retrieve the characters.');
				return;
			}
			else
			{
				var text = '*Characters*';
				result.forEach(function(character) {
					text = text + '\n- ' + character.name;
				});
				bot.say({ text: text, channel: message.channel });
			}
		});
	}
);

// choose a character
controller.hears(
	['^my character is \".*\"$'],
	['direct_mention', 'mention', 'ambient'],
	function(bot, message) {
		var character;
		
		// extract the name of the character
		var name = message.text.split(/[""]/)[1];
		
		// validate it
		if (!name.length || name.length === 0)
		{
			bot.reply(message, 'Sorry, <@' + message.user + '>, that is not a valid character name.');
			return;
		}

		// see if that character exists
		db_collection_characters.find({ name: name }).toArray(function (error, result) {
			if (error)
			{
				bot.reply(message, 'Sorry, <@' + message.user + '>, I wasn\'t able to determine if that character exists.');
				return;
			}
			else
			{
				character = result[0];

				db_collection_players.update({ _id: message.user }, { $set: { 'character': character.name }}, { upsert: true }, function (error, result) {
					if (error)
					{
						bot.reply(message, 'Sorry, <@' + message.user + '>, I wasn\'t able to set that as your character.');
						return;
					}
					else
					{
						// reply with the user's new title
						bot.reply(message, 'Alright, <@' + message.user + '>, your character is ' + name + '!');
					}
				});
			}
		});
	}
);

// choose a name
controller.hears(
	['^my name is \".*\"$'],
	['direct_mention', 'mention', 'ambient'],
	function(bot, message) {
		var character;

		// extract the name
		var name = message.text.split(/[""]/)[1];
		
		// validate it
		if (!name.length || name.length === 0)
		{
			bot.reply(message, 'Sorry, <@' + message.user + '>, that is not a valid character name.');
			return;
		}

		db_collection_players.update({ _id: message.user }, { $set: { 'name': name }}, { upsert: true }, function (error, result) {
			if (error)
			{
				bot.reply(message, 'Sorry, <@' + message.user + '>, I wasn\'t able to set that as your name.');
				return;
			}
			else
			{
				// reply with the user's new title
				bot.reply(message, 'Alright, <@' + message.user + '>, your name is ' + name + '!');
			}
		});
	}
);

// game results
controller.hears(
	['^(played \\d+ games)((,\\s(<@\\w+>)\\s([0-9]+))+)$'],
	['direct_mention'],
	function(bot, message) {
		var components = message.text.split(",");

		// get the number of games played
		var game_count = parseInt(components[0].split(" ")[1]);

		var round = {
			games: parseInt(game_count),
			datetime: Date.now(),
			scores: [
			]
		};

		for (var i = 1; i < components.length; ++i) {
			var player_score = {
				player_id: components[i].split(" ")[1].split(/[@>]/)[1],
				score: components[i].split(" ")[2],
				average: (parseInt(components[i].split(" ")[2]) / game_count).toFixed(2)
			};

			round.scores.push(player_score);
		}

		db_collection_games.insert(round, function(error, result) {
			if (error)
			{
				bot.reply(message, 'Sorry, I wasn\'t able to save that round.');
				return;
			}
			else
			{
				bot.reply(message, 'The round has been logged.');

				var players = db_collection_players.find().toArray(function (error, result) {

					var text = 'You played ' + game_count + ' games. The scores were: ';

					for (var i = 0; i < round.scores.length; ++i)
					{
						var player = result.filter(function(player) { return (player._id === round.scores[i].player_id) })[0];
						text += ('\n' + player.name + ': ' + round.scores[i].score);
					}

					bot.reply(message, text);
				});
			}
		});
	}
);

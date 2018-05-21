const Discord = require('discord.js');
const https = require('https');
const http = require('http');
const htmlSoup = require('html-soup');
const fs = require('fs');
const bot = new Discord.Client()
const json = 'penelope.json';

let memoire = {};
fs.readFile(json,'utf-8', (err, json)=>{
	let obj = JSON.parse(json);
	for (i in obj.initmem) {
		usecommand(obj.initmem[i],memoire);
	}
});

String.prototype.replaceAll = function(search, replacement) {
    var target = this;
    return target.replace(new RegExp(search, 'g'), replacement);
};

bot.on('message', function(msg) {
	if (msg.author.username != "UlysseBOT") {
		respond(msg, json ,(res) => {
			msg.channel.send(res);
		});
	}
});

bot.login('Mzc2MDI2MTU4Njg2MjczNTM2.DN4ZMQ.5Q_n4RDlEl_QiyxP2BXprrQYh1A');


function httpget(url, thecallback) {
	if (url.substring(0,8) == "https://") {
		https.get(url, res => {
			res.setEncoding("utf-8");
			let body = "";
			res.on("data", (data) => {
				body += data;
			})
			res.on("end", () => {
				thecallback(body);
			})
		})
	}
	else if (url.substring(0,7) == "http://") {
		http.get(url, res => {
			res.setEncoding("utf-8");
			let body = "";
			res.on("data", (data) => {
				body += data;
			})
			res.on("end", () => {
				thecallback(body);
			})
		})
	}
}

function respond(msg,jsonfile,callback) {
	fs.readFile(jsonfile,'utf-8', (err, json)=>{
		let obj = JSON.parse(json);
		let behaviors = obj.behaviors;
		let role;
		let commands;


		for (key in obj.roles) {
			for (iuser in obj.roles[key]) {
				user = obj.roles[key][iuser];
				if (user == msg.author.username) {
					role = key;
				}
			}
		}

		if (role == undefined) {
			role = "common";
		}
		for (i in behaviors) {
			let ibehavior = behaviors[i];
			for (j in ibehavior.in) {
				let intext = ibehavior.in[j].replaceAll(" ","").toUpperCase();
				let msgtext = msg.content.replaceAll(" ","").substring(0,intext.length).toUpperCase();
				if (intext == msgtext) {
					let rightkey;
					let ibehaviorout = ibehavior.outs
					for (key in ibehaviorout) {
						let parts = key.split(" ");
						if (memoire[parts[0]]== parts[1]) {
							rightkey = key;
						}
					}
					rightkey = rightkey != undefined ? rightkey : "c";
					for (com in ibehavior.commands) {
						usecommand(ibehavior.commands[com],memoire);
					}
					var indexrole = typeof ibehavior.roles == 'undefined' ? 0 : ibehavior.roles.indexOf(role);
					var roleouts = ibehaviorout[rightkey][indexrole];
					console.log(rightkey);
					var randomindex = Math.floor(Math.random()*roleouts.length);
					callback(roleouts[randomindex]);
				}
			}
		}
	});
}


function usecommand(command, memory) {
	console.log(command)
	let parts = command.split(" ");
	if (parts[0] == "set") {
		memory[parts[1]] = parts[2]
	}
}
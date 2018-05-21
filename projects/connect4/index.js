var express = require('express');
var socket = require('socket.io');

var app = express();
var server = app.listen(3000);
app.use(express.static('public'));
var io = socket(server);

console.log("serveur en marche");
var turn = 1;
var map = new Array(7);
for (i=0;i<map.length;i++) {
	map[i] = new Array(6);
	for (j=0;j<map[i].length;j++) {
		map[i][j]=0;
	}
}



var connections = [];

function play(x,y,p,callback) {
	if (p==turn) {
		if (map[x][5] == 0) {
			let high = 5;
			for (i=0;i<6;i++) {
				if (map[x][i] == 0 && i<high) {
					high = i;
				}
			}
			map[x][high] = p;
			if (turn==1) {
				turn=2;
			}
			else if (turn == 2) {
				turn=1;
			}
			callback("Okay");
		}
		else {
			callback("colonne deja pleine");
		}
	}
	else {
		callback("pas ton tour");
	}
}

io.on('connection', (socket) => {
	let id = socket.id.slice(-4);
	connections.push(id);
	console.log(connections);
	socket.on('map', () => {
		socket.emit('mapres',map);
	})
	socket.on('play', (data) => {
		data.p = connections.indexOf(id)+1;
		console.log(data);
		play(data.x,data.y,data.p, (message) => {
			console.log(message);
			socket.emit('playres',message);
		})
		io.sockets.emit('mapres',map);
	});
	socket.on('disconnect', () => {
		let index = connections.indexOf(id);
		connections.splice(index);
		console.log(connections);
	});
});
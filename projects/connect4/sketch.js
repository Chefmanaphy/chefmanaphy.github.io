
let socket;

function setup() {
	let cnv = createCanvas(700, 600);
	cnv.style.float = "left";
	cnv.parent('canvasholder');
	socket = io.connect('192.168.43.165:3000');
	socket.on('playres', showmessage);
	socket.on('mapres', updatemap);
	socket.emit('map', null);
	background(170);
	begin();
}

function draw() {

}

function drawgrid() {
	strokeWeight(5);
	fill(200);
	for (i=0;i<7;i++) {
		for (j=0;j<6;j++) {
			rect(i*width/7,j*height/6,width/7-1,height/6-1);
		}
	}	
}

function begin() {
	drawgrid();
}

function mousePressed() {
	playerClick(mouseX,mouseY);
}

function playerClick(x,y) {
	if (x>=0 && x<width && y>=0 && y<height) {
		data = {
			x:Math.floor(x*7/width),
			y:5-Math.floor(y/(height/6))
		}
		sendtoserver(data);
	}
}

function sendtoserver(data) {
	socket.emit('play', data);
}

function play(x,y,p) {
	if (p==1) {
		fill(255,0,0);
		ellipse(x*width/7+width/14,(5-y)*height/6+height/12,width/7);
	}
	else if (p==2) {
		fill(255,255,0);
		ellipse(x*width/7+width/14,(5-y)*height/6+height/12,width/7);
	}
}

function updatemap(data) {
	drawgrid();
	for (i=0;i<data.length;i++) {
		for (j=0;j<data[i].length;j++) {
			play(i,j,data[i][j]);
		}
	}
}

function showmessage(message) {
	console.log(message);
	document.getElementById("message").innerHTML = message;
}
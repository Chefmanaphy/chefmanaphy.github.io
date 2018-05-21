let ball;
function setup() {
	createCanvas(500, 500);
	ball = new Tile();
	ball.setPos(width/2,height/2);
	ball.setAcc(0,0.15);
	ball.setVel(6,0);
}

function draw() {
	background(255);
	if (ball.getPos().x<0 || ball.getPos().x>width) {
		ball.setVel(ball.getVel().x*-1,ball.getVel().y);
	}
	ball.update();
	ball.display();
}
function mousePressed() {
	ball.setVel(ball.getVel().x,-5);
}

let a,rockets;
function setup() {
	createCanvas(500, 500);
	s1 = createSlider(0,1.0, 1, 0.01);
	s2 = createSlider(0,1.0, 0, 0.01);
	s3 = createSlider(0,1.0, 0, 0.01);
	rockets = [];
	for (let i=0;i<50;i++) {
		rockets[i] = new Rocket((i-25)*8,height/2,s1,s2,s3);
	}
}

function draw() {
	background(255);
	translate(width/2,height/2);
	for (let rocket of rockets) {
		rocket.update();
		rocket.display();
		rocket.showVecs();
	}

}

function mousePressed() {
	// a.vel.x-=0.1;
}

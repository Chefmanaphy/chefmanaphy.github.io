var shape = true;

function setup() {
	createCanvas(500, 500);
	stroke(0);
	strokeWeight(16);
	fill(255);
}

function draw() {
	display();
}

function display() {
	background(255);
	translate(width/2,height/2);

	var spacing = 2*PI/360;
	pointscir = [];
	pointstri = [];
	pointsmorph = [];
	radius = 200;

	for (i=0;i<2*PI;i+=spacing) {
		if (i>2*PI) {
			i-=2*PI;
		}

		var cirx = cos(i);
		var ciry = sin(i);
		var cirv = new p5.Vector(cirx,ciry);
		cirv = cirv.mult(radius);
		pointscir.push(cirv);

		if (i<2*PI*1/3) {
			var trix = (-sin(2*PI*1/3)/(-1.5))/(tan(i)-sin(2*PI*1/3)/(-1.5));
		}
		else if (i<2*PI*2/3) {
			var trix = -0.5;
		}
		else {
			var trix = (-sin(2*PI*1/3)/(1.5))/(tan(i)-sin(2*PI*1/3)/(1.5));
		}
		var triy = tan(i)*trix
		var triv = new p5.Vector(trix,triy);
		triv = triv.mult(radius);
		pointstri.push(triv);

		var amt = (sin(frameCount/30)+1)/2;
		var cirtri = new p5.Vector(trix-cirx,triy-ciry);
		var morv = new p5.Vector(cirx+cirtri.x*amt,ciry+cirtri.y*amt);
		morv = morv.mult(radius);
		pointsmorph.push(morv);
	}



	//drawing
	beginShape();
	for (i=0;i<pointsmorph.length;i++) {
		vertex(pointsmorph[i].x,pointsmorph[i].y);
	}
	endShape(CLOSE);
}

function mousePressed() {
	shape = !shape;
}
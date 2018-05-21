let xc =8;
let yc =8;
let speed = 1;
let ga;
let x = 0;
let imgcount = 0;
let end;
let dots;
let pretty;

function setup() {
	createCanvas(800, 800);

	NeuralNetwork.count=0 ;
	Matrix.count=0 ;

	dots = [];
	end = false;
	pretty = true;

	ga = new GeneticAlgorithm(xc*yc, width/xc, height/yc);
	// ga.todowithmax = (maxscore)=>{point(x, height-maxscore/3);x++;};
	background(255);
}

function draw() {
	if (!pretty) {
		background(255);
		strokeWeight(2);
		stroke(0);
		for (let vec=0;vec<dots.length-1;vec++) {
			line(dots[vec].x,height-dots[vec].y/3, dots[vec+1].x, height-dots[vec+1].y/3);
		}
	}
	else {
		display();
	}
	if (!end) {
		play();
	}
}

function display() {
	background(255);
	for (let i = 0;i<xc*yc;i++) {
		let theobj = ga.population[i].indiv;
		theobj.display();
		image(theobj.graphics,(i%xc)*(width/xc),Math.floor(i/xc)*(height/yc));
	}
}

function mousePressed() {
	pretty = !pretty;
		// console.log(Matrix.count) ;
		// end = true;
		// console.log(ga);
}

function play() {
	for (let i=0;i<speed;i++) {
		ga.step();
	}
}

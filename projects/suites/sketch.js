function setup() {
	createCanvas(500, 500);
	strokeWeight(5);
	background(255);

	let un = [1];

	let vn = [];

	let u = (un1,n) => {
		return 0.5*un1-1;
	};

	let v = (un, n) => {
		return un[n+1]-un[n];
	};

	for (let i=1;i<50;i++) {un.push(u(un[i-1], i));}
	for (let i=0;i<49;i++) {vn.push(v(un, i));}
	stroke(0,255,0);
	for (let i = 0;i<un.length;i++) {
		point(i*10+5, height/2-(un[i])*100);
	}
	stroke(0,0,255);
	for (let i = 0;i<49;i++) {
		point(i*10+5, height/2-(vn[i])*100);
		console.log(vn[i]);
	}

}

function draw() {


}

let a;
function setup() {
	createCanvas(32,32);
	background(255);
	a = new Brain([2,7,9,2,6,3]);
	let values = [];
	for (let i=0;i<width;i++) {
		for (let j=0;j<height;j++) {
			let out = a.forwardprop([i/width,j/height]);
			values.push({"x" : i, "y" : height - j, "val" : out});
		}
	}
	let mins = [1,1,1];
	let maxs = [0,0,0];
	for (let value of values) {
		thevalue = value.val.flatten().dataSync();
		for (let i=0;i<thevalue.length;i++) {
			if (maxs[i] < thevalue[i]) {maxs[i] = thevalue[i];}
			if (mins[i] > thevalue[i]) {mins[i] = thevalue[i];}
		}
	}
	console.log(maxs);
	console.log(mins);
	for (let value of values) {
		thevalue = value.val.flatten().dataSync();
		// stroke(map(thevalue[0],mins[0],maxs[0],0,256),map(thevalue[1],mins[1],maxs[1],0,256),map(thevalue[1],mins[1],maxs[1],0,256));
		stroke(0,map(thevalue[1],mins[1],maxs[1],0,256),0);
		point(value.x,value.y);

	}

	// stroke(out[0]*256, out[1]*256, out[2]*256);
	// point(i*width, height - j * height);
}

function draw() {

}

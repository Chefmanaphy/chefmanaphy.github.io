let point, img;

function setup() {
	createCanvas(600, 600);
	// Decimal.set({ precision: 100 })
	img = createGraphics(600,600);
	let x = new Decimal(0.106822593694416330);
	let y = new Decimal(0.637372649293168275);
	point = [x,y];

}

function draw() {
	if (frameCount > 0) {
		let delta = new Decimal(1).div(new Decimal(frameCount).div(new Decimal(5)).exp());
		let minx = point[0].minus(delta).toNumber();
		let maxx = point[0].plus(delta).toNumber();
		let miny = point[1].minus(delta).toNumber();
		let maxy = point[1].plus(delta).toNumber();
		drawMandelbrot(img,[minx,maxx],[miny,maxy], 2000);
		image(img,0,0);
	}
}

function drawMandelbrot(gr, xrange, yrange, maxiter) {
	gr.loadPixels();
	for(let x=0;x<gr.width;x++) {
		for(let y=0;y<gr.height;y++) {

			let mx = map(x,0,gr.width,xrange[0], xrange[1]);
			let my = map(y,gr.height,0,yrange[0], yrange[1]);
			let thecolor = getColorInMandelbrot(mx,my,maxiter);

			let ind = (x+y*gr.width)*4;

			gr.pixels[ind + 0] = thecolor[0];
			gr.pixels[ind + 1] = thecolor[1];
			gr.pixels[ind + 2] = thecolor[2];
			gr.pixels[ind + 3] = 255;
		}
	}
	gr.updatePixels();


	function getColorInMandelbrot(x, y, maxiter) {
		let n = 0;
		let a = x;
		let b = y;

		while (n < maxiter) {
			let na = a*a - b*b;
			let nb = 2*a*b;

			a = na+x;
			b = nb+y;

			if (a+b > 2000) {
				break;
			}
			n++;
		}

		let value = map(n,0,maxiter,0,1);
		// value = sqrt(value);
		let thecolor = HSVtoRGB(value,0.6,1);
		if (n == maxiter) {thecolor = {r:0,g:0,b:0};}
		thecolor = [thecolor.r, thecolor.g, thecolor.b];
		return thecolor;
	}

}

function HSVtoRGB(h, s, v) {
    var r, g, b, i, f, p, q, t;
    if (arguments.length === 1) {
        s = h.s, v = h.v, h = h.h;
    }
    i = Math.floor(h * 6);
    f = h * 6 - i;
    p = v * (1 - s);
    q = v * (1 - f * s);
    t = v * (1 - (1 - f) * s);
    switch (i % 6) {
        case 0: r = v, g = t, b = p; break;
        case 1: r = q, g = v, b = p; break;
        case 2: r = p, g = v, b = t; break;
        case 3: r = p, g = q, b = v; break;
        case 4: r = t, g = p, b = v; break;
        case 5: r = v, g = p, b = q; break;
    }
    return {
        r: Math.round(r * 255),
        g: Math.round(g * 255),
        b: Math.round(b * 255)
    };
}

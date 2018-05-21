<script>
	var canvas;
	var c;
	var width;
	var height;
	var framecount = 0;
	var trons = [];
	function bg() {
		window.setInterval(function(){
			draw();
		}, 1000/60);
		canvas = document.getElementById("bg");
		c = canvas.getContext("2d");
		canvas.width=window.innerWidth;
		canvas.height=window.innerHeight;
		width = canvas.width;
		height = canvas.height;
		for (var i = 0;i<200;i++) {
			trons[i] = new Tron(width,height);
		}
	}

	window.addEventListener('resize', function(event){
		canvas.width=window.innerWidth;
		canvas.height=window.innerHeight;
		width = canvas.width;
		height = canvas.height;
		for (var i = 0;i<trons.length;i++) {
			trons[i].def();
		}
	});



	function draw() {
		framecount++;
		c.fillStyle = "#000000";
		c.globalAlpha = 0.07;
		c.fillRect(0,0,width,height);
		c.globalAlpha = 1;
		for (var i=0;i<trons.length;i++) {
			trons[i].display();
		}
	}

	function Tron() {
		this.def = function() {
			this.x = Math.random()*width*0.9+width*0.05;
			this.y = Math.random()*height*0.9+height*0.05;
			this.direction = Math.floor(Math.random()*4);
			this.hue = Math.floor(Math.random()*256);
		}
		this.def();
		this.display = function() {
			var s = Math.sin((255-this.hue+framecount/2%255)/255*2*Math.PI)*30;
			if (s<0){s=0;}
			if (this.direction==0) {this.x+=1;}
			if (this.direction==1) {this.y+=1;}
			if (this.direction==2) {this.x-=1;}
			if (this.direction==3) {this.y-=1;}
			if (Math.floor(Math.random()*11)==5) {this.direction = Math.floor(Math.random()*4);}
			var color = HSVtoRGB(this.hue/255,255/255,255/255);
			c.fillStyle = rgb2hex(color);
			c.lineWidth = 0.00001;
			fillCircle(this.x,this.y,s+5);
			if (this.x<0 || this.y<0 || this.x>width || this.y>height) {this.def();}
		}
	}

	function fillCircle(x,y,s) {
		c.beginPath();
		c.arc(x,y,s,0,2*Math.PI,false);
		c.stroke();
		c.fill();
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
		r = Math.round(r*255);
		g = Math.round(g*255);
		b = Math.round(b*255);
		return ("rgb("+r+","+g+","+b+")");
	}
	function rgb2hex(rgb){
		rgb = rgb.match(/^rgba?[\s+]?\([\s+]?(\d+)[\s+]?,[\s+]?(\d+)[\s+]?,[\s+]?(\d+)[\s+]?/i);
		return (rgb && rgb.length === 4) ? "#" +
		("0" + parseInt(rgb[1],10).toString(16)).slice(-2) +
		("0" + parseInt(rgb[2],10).toString(16)).slice(-2) +
		("0" + parseInt(rgb[3],10).toString(16)).slice(-2) : '';
	}
</script>

<canvas id="bg"></canvas>

<script>bg();</script>

<style>
	body{
		margin:0;
		padding:0;
	}
	canvas{
		position:fixed;
		left:0;
		top:0;
		z-index:-1;
		background-color:#000000;
	}
</style>
var mic, fft,osc;
var playing = false;
var shape = 0;
var shapes = ["sine","triangle","sawtooth","square"];
function setup() {
	createCanvas(1024,400);
	noFill();
	osc = new p5.Oscillator();
	osc.setType(shapes[shape]); //type of oscillator. Options: 'sine' (default), 'triangle', 'sawtooth', 'square'
	osc.amp(0.1);
	osc.freq(375);
	osc.start();
	fft = new p5.FFT();
	fft.setInput(osc);
	let slider = document.getElementsByTagName("input")[0];
	let p = document.getElementsByTagName("p")[0];
	slider.onchange = () => {
		console.log(slider.value);
		p.innerHTML = slider.value;
		osc.freq(parseInt(slider.value));
	};
}


function draw() {
   background(200);

   var spectrum = fft.waveform();

   beginShape();
   // console.log(spectrum);
   for (i = 0; i<spectrum.length; i++) {
    vertex(i, map(spectrum[i], -0.1, 0.1, height, 0) );
   }
   endShape();
}
function mouseClicked() {
  if (mouseX > 0 && mouseX < width && mouseY < height && mouseY > 0) {
	if (mouseButton == "right") {
		if (!playing) {
		  // ramp amplitude to 0.5 over 0.05 seconds
		  osc.start();
		  playing = true;
		} else {
		  // ramp amplitude to 0 over 0.5 seconds
		  osc.stop();
		  playing = false;
		}
	}
	else {
		shape++;
		osc.setType(shapes[shape%shapes.length]);
	}
  }
}
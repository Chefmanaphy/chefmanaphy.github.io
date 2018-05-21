let alphabet = {
	"a":". _",
	"b":"_ . . .",
	"c":"_ . _ .",
	"d":"_ . .",
	"e":".",
	"f":". . _ .",
	"g":"_ _ .",
	"h":". . . .",
	"i":". .",
	"j":". _ _ _",
	"k":"_ . _",
	"l":". _ . .",
	"m":"_ _",
	"n":"_ .",
	"o":"_ _ _",
	"p":". _ _ .",
	"q":"_ _ . _",
	"r":". _ .",
	"s":". . .",
	"t":"_",
	"u":". . _",
	"v":". . . _",
	"w":". _ _",
	"x":"_ . . _",
	"y":"_ . _ _",
	"z":"_ _ . .",
	" ":"       "
}
let song;
let speed = 100;
let time = 0;
function setup() {
	song = loadSound("bip.wav");
}

function submitt() {
	let input = document.getElementById("input").value;
	document.getElementById("input").value = "";
	let output = encode(input);
	document.getElementById("output").innerHTML += "\n"+output;
	let instructs = [];
	playsound(0);
	for (i of output) {
		switch(i) {
			case " ":
				setTimeout(()=>{song.play()},time);
				setTimeout(()=>{song.stop()},time+0*speed);
				time+=1*speed;
				break;
			case ".":
				setTimeout(()=>{song.play()},time);
				setTimeout(()=>{song.stop()},time+1*speed);
				time+=1*speed;
				break;
			case "_":
				setTimeout(()=>{song.play()},time);
				setTimeout(()=>{song.stop()},time+3*speed);
				time+=3*speed;
				break;
		}
		time+=10;
	}
}

function encode(input) {
	let res = "";
	for (i of input) {
		res+=alphabet[i];
		res+= "   ";
	}
	return(res);
}

function playsound(time) {
	song.play();
	setTimeout(()=>{song.stop()},time);
}
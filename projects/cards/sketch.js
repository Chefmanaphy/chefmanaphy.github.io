function main() {
	g = new Game()
	g.addgameset("52");
	g.addplayer("Chefmanaphy");
}
class Game{
	constructor() {
		this.turns = 0;
		this.round = 0;
		this.gamesets = {};
		this.players = {};
		this.flog = "";
		this.log = "";
	}
	addgameset(mode,name="gameset") {
		this.gamesets[name] = new Gameset(this,mode);
	}
	addplayer(player,role="defaut"){
		this.players[player] = new Player(this,player,role);
	}
}

class Player{
	constructor(game,name,role) {
		this.cards = {};
		this.name = name;
		this.game = game;
		this.role = role;
		this.nb = null;
		this.onrefresh = function () {}
		this.refresh()
	}
	refresh() {
		this.nb = this.count(this.cards);
		this.onrefresh();
	}
	count(cards) {
		console.log(cards);
		return(Object.keys(cards).length);
	}
	giverandom(player) {
		let rand = Math.floor(Math.random()*this.nb);
		let cardname = Object.keys(this.cards)[rand];
		let card = this.cards[cardname];
		this.give(card,player);
	}
	give(card,player) {
		console.log(card);
		card.setOwner(player);
		delete this.cards[card.name]
		player.cards[card.name]=card;
		this.refresh();
		player.refresh();
	}
}
 
class Gameset extends Player{
	constructor(game,mode,name="gameset",role="gameset") {
		super(game,name,role);
		this.cards = {}
		switch (mode) {
			case "52" : this.cards = this.fillgameset52(); break;
		}
		this.refresh()
	}
	fillgameset52() {
		let res = {};
		for (let weight=0;weight<13;weight++) {
			for (let color=0;color<4;color++) {
				let card = new Card(this,weight,color);
				let name = card.name;
				res[name]=card;
			}
		}
		return(res);
	}
} 

class Card{
	constructor(Gameset, weight, color) {
		this.gameset = Gameset;
		this.owner = Gameset;
		this.weight = weight;
		this.color = color;
		this.name = this.setname(weight,color).nm;
		this.fname = this.setname(weight,color).fnm;
	}
	setOwner(owner) {
		this.owner=owner;
	}
	setname(weight, color) {
		let name = "";
		let fname = "";
		if (weight < 10 && weight>0) {
			name = (weight+1).toString();
			fname = (weight+1).toString();
		}
		else {
			switch(weight) {
				case 0:
					name = "A"
					fname = "As";
					break;
				case 10:
					name = "V";
					fname = "Vallet";
					break;
				case 11:
					name = "D";
					fname = "Dame";
					break;
				case 12:
					name = "R";
					fname = "Roi";
			}
		}
		fname+=" de ";
		switch(color) {
			case 0:
				name+="H";
				fname+="coeur";
				break;
			case 1:
				name+="C";
				fname+="carreau";
				break;
			case 2:
				name+="P";
				fname+="pique";
				break;
			case 3:
				name+="T";
				fname+="trefle";
		}
		return({nm : name, fnm : fname});
	}
}

function setup() {
	createCanvas(windowWidth, windowHeight);
	main();

}

function draw() {

}
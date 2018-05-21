class Fen2048 {
  constructor(w,h) {
    this.brain = new NeuralNetwork(17,64,4);
    this.reset(w,h);
  }

  reset(w,h) {
    this.grid = new Matrix(4,4);
    this.processed = false;
    this.score = 0;
    this.movecount = 0;
    this.losed = false;
    this.grid.data[1][0] = 2;
    this.grid.data[3][1] = 2;
    this.uselessmoves = [];
    if (w && h) {
      this.graphics = createGraphics(w,h);
    }
    else {
      this.graphics = createGraphics(100,100);
    }

  }

  think() {
		if (!this.losed) {
			let cases = normalize(this.grid.toArray());
      cases[16] = this.movecount;
			let out = this.brain.predict(cases);
      cases = null;
			for (let i of this.uselessmoves) {
				out[i]=-2;
			}
			let dir = out.indexOf(Math.max.apply(null,out));
			this.play(dir);
		}
  }

  play(dir) {
    if (!this.losed) {
      let initgrid = this.grid.copy();
      let dirx = 0;



      let diry = 0;
      if (dir==0) {dirx = 1;}
      if (dir==1) {diry = -1;}
      if (dir==2) {dirx = -1;}
      if (dir==3) {diry = 1;}

      if (dir == 0) {
        for (let x = 2;x>=0;x--) {
          for (let y = 0;y<4;y++) {
            this.move(x,y,dirx,diry);
          }
        }
      }
      if (dir == 1) {
        for (let y = 1;y<4;y++) {
          for (let x = 0;x<4;x++) {
            this.move(x,y,dirx,diry);
          }
        }
      }
      if (dir == 2) {
        for (let x = 1;x<4;x++) {
          for (let y = 0;y<4;y++) {
            this.move(x,y,dirx,diry);
          }
        }
      }
      if (dir == 3) {
        for (let y = 2;y>=0;y--) {
          for (let x = 0;x<4;x++) {
            this.move(x,y,dirx,diry);
          }
        }
      }
      let freecases = this.grid.count(0);
      if (freecases.length==0) {
        let losed = true;
        for (let y = 0;y<4;y++) {
          for (let x = 0;x<4;x++) {

            let thecase = this.grid.data[x][y];
            if (y-1>=0) {if (thecase==this.grid.data[x][y-1]) {losed = false;}}
            if (x-1>=0) {if (thecase==this.grid.data[x-1][y]) {losed = false;}}
            if (y+1<4) {if (thecase==this.grid.data[x][y+1]) {losed = false;}}
            if (x+1<4) {if (thecase==this.grid.data[x+1][y]) {losed = false;}}

          }
        }
        if (losed){
          this.losed = losed;
          this.score = this.grid.sum();
        }
      }
      let moved = this.grid.compare(initgrid);
      initgrid = null;
      if (!moved) {
        let newcase = freecases[Math.floor(Math.random()*freecases.length)];
        this.movecount++;
        this.grid.data[newcase[0]][newcase[1]] = Math.floor(Math.random()*2+1)*2;
        this.uselessmoves = [];
      }
      else {if(this.uselessmoves.indexOf(dir) == -1) {this.uselessmoves.push(dir);}}
    }
  }

  move(x,y,dirx, diry) {
    let stopped = false;
    let thiscase = this.grid.data[x][y];
    let nx = x;
    let ny = y;
    do {
      nx+=dirx;
      ny+=diry;
      if (this.grid.data[nx][ny] == thiscase || this.grid.data[nx][ny] == 0) {
        if (this.grid.data[nx][ny] == thiscase) {
          stopped = true;
        }
        this.grid.data[nx-dirx][ny-diry] = 0;
        this.grid.data[nx][ny] += thiscase;
      }
      else {
        stopped = true;
      }
    } while(nx+dirx >= 0 && ny+diry >= 0 && nx+dirx <= 3 && ny+diry<=3 && !stopped)
  }

  display() {
    let w = this.graphics.width;
    let h = this.graphics.height;
    this.graphics.background(255,255,200);
    let ls = w>h?h:w;
    for (let y=0;y<4;y++) {
      for (let x=0;x<4;x++) {
        this.graphics.stroke(200,200,200);
        this.graphics.strokeWeight(ls/20);
        this.graphics.noFill();
        this.graphics.rect(x*w*0.25,y*h*0.25,w*0.25,h*0.25);
        this.graphics.noStroke();
        this.graphics.textAlign(CENTER, CENTER);
        this.graphics.textSize(ls/10);
        let number = this.grid.data[x][y];
        if (number != 0) {this.graphics.fill(0);}
        this.graphics.text(number,x*w*0.25+w*0.125,y*h*0.25+h*0.125);
      }
    }
		if (this.losed) {
			this.graphics.fill(0, 128);
			this.graphics.rect(0,0,w,h);
		}
    this.graphics.noFill();
    this.graphics.stroke(255,0,0);
    this.graphics.strokeWeight(ls/40);
    this.graphics.rect(0,0,w,h);
  }
}

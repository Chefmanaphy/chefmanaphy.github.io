class Tile {
  constructor() {
    self.pos = new p5.Vector();
    self.vel = new p5.Vector();
    self.acc = new p5.Vector();
    self.diameter = 10;
  }
  setAcc(x,y) {self.acc = new p5.Vector(x,y);}
  getAcc() {return(self.acc)}
  setVel(x,y) {self.vel = new p5.Vector(x,y);}
  getVel() {return(self.vel)}
  setPos(x,y) {self.pos = new p5.Vector(x,y);}
  getPos() {return(self.pos)}
  update() {
    self.vel.add(self.acc);
    self.pos.add(self.vel);
  }
  display() {
    rectMode(CENTER);
    rect(self.pos.x,self.pos.y,self.diameter,self.diameter);
  }
}

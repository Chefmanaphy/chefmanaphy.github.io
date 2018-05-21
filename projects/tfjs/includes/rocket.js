class Rocket {
  constructor(x,y,s1,s2,s3) {
    this.pos = new p5.Vector(x,y);

    this.dir = 0;

    this.graphs = createGraphics(4,25);
    this.graphs.fill(255,0,0);
    this.graphs.noStroke();
    this.graphs.rect(0, 3, 4,25);
    this.graphs.ellipse(2,2,3,3);

    this.potentiometers = [s1,s2,s3];

    this.vel = new p5.Vector(0,0);

    this.reactors = [];
    this.reactors.push(new p5.Vector(0,-0.02).rotate(0));
    this.reactors.push(new p5.Vector(0,-0.02).rotate(TWO_PI/3));
    this.reactors.push(new p5.Vector(0,-0.02).rotate(2*TWO_PI/3));

    this.reaccoms = [1,0,0];

    this.vecs = [];
  }

  showVecs() {
    strokeWeight(2);
    stroke(0);
    for (let vec of this.vecs) {
      line(this.pos.x,this.pos.y,this.pos.x-vec.x*3000,this.pos.y-vec.y*3000);
    }
  }

  display() {
    fill(128,0,0);
    noStroke();
    push();
    translate(this.pos.x-2,this.pos.y);
    rotate(this.dir);
    image(this.graphs,0,0);
    pop();
    ellipse(this.pos.x,this.pos.y,4,4);
  }

  update() {
    this.reaccoms[0] = this.potentiometers[0].value()
    this.reaccoms[1] = this.potentiometers[1].value()
    this.reaccoms[2] = this.potentiometers[2].value()
    let acc = new p5.Vector(0,0.001);
    for (let i=0;i<this.reactors.length;i++) {
      this.vecs[i] = this.reactors[i].copy();
      this.vecs[i].mult(this.reaccoms[i]*0.1);
      this.vecs[i].rotate(this.dir);
      acc.add(this.vecs[i]);
    }
    this.vel.add(acc);
    this.dir = this.vel.heading()+PI/2;


    this.pos.add(this.vel);
  }
}

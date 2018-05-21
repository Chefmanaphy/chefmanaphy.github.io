

class Brain {

  constructor(shape) {
    this.shape = shape;
    this.outputs = undefined;
    this.layers = [];
    this.layers.push(new Layer(this, 0, shape[0]));
    for (let i=1;i<this.shape.length;i++) {
      this.layers.push(new Layer(this, i,shape[i], this.layers[i-1]));
    }
  }
  fordwardprop(inputs) {
    this.layers[0].setInputs(inputs);
    for (let i=1;i<this.layers.length;i++) {
      this.layers[i].calculate();
    }
    return this.outputs[0];
  }

}

class Layer {
  constructor(brain, id, nodecount, previouslayer = null) {
    this.brain = brain;
    this.id = id;
    this.nc = nodecount;
    this.values = undefined;
    if (previouslayer) {
      this.pl = previouslayer;
      this.weights = new Matrix(nodecount, previouslayer.nc).map(()=>(Math.random()*2)-1);
      this.bias = new Matrix(nodecount,1).map(()=>(Math.random()*2)-1);
    }
  }

  setInputs(inputs) {
    this.values = Matrix.fromArray(inputs);
  }

  calculate() {
    this.values = Matrix.multiply(this.weights,this.pl.values).add(this.bias).map(sigmoid); //calcule les valeurs de ce layer
    if (this.id == this.brain.shape.length-1) {
      this.brain.outputs = this.values.data;
    }
  }
}

function sigmoid(x,_,_) {
  return 1/(1+Math.exp(-x));
}

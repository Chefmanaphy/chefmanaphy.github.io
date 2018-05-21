class GeneticAlgorithm {
  constructor(popsize, w, h) {

    this.w = w;
    this.h = h;

    this.generationcount = 0;

    this.popsize = popsize;

    // this.todowithmax = ()=>{};


    // this.stepfunction = stepfunction;
    // this.checkoverfunction = checkoverfunction;
    // this.getfitnessfunction = getfitnessfunction;

    this.populationmake();
  }

  populationmake() {
    //making the population
    this.population = [];
    for (let i=0;i<this.popsize;i++) {
      this.population.push({indiv : new Fen2048(this.w,this.h), nfit : undefined, accnfit : undefined});
    }
  }

  step() {
    //fait agir les individus jusqu'a qu'ils aient tous un resultat
    let over = true;

    for (let individu of this.population) {
      individu.indiv.think();
      if (!individu.indiv.losed) {over = false;}
    }

    if (over) {
      //new generation
      let winners = this.selection();
      let newpopulation = this.crossover(winners);
      this.population = this.mutate(newpopulation);
      this.generationcount++;
    }
  }

  selection() {
    let survivors = [];
    let totalfitness = 0;
    for (let individu of this.population) {
      let thefitness = individu.indiv.score;
      totalfitness+=thefitness;
    }
    dots.push(new p5.Vector(x, totalfitness/this.popsize));


    for (let i=0;i<Math.floor(this.popsize/8);i++) {
      survivors.push(this.pickone(this.population));
    }
    x++;
    if (x>width) {
      saveCanvas("result"+imgcount+".png");
      background(255);
      imgcount++;
      dots = [];
      x=0;
    }


    return survivors;
  }

  crossover(survivors) {
    //select the parents and reproduct them
    let parentscount = 2;
    let children = [];
    for (let i=0;i<this.popsize-survivors.length;i++) {
      let parents = [];
      let survivorscopy = [];
      for (let survivor of survivors) {survivorscopy.push(survivor);}
      parents.push(this.pickone(survivorscopy));
      parents.push(this.pickone(survivorscopy));
      children.push(this.reproduct(parents, this.population[i]));
    }
    for (let survivor of survivors) {survivor.indiv.reset()}
    let newpopulation = survivors.concat(children);
    return newpopulation;
  }

  reproduct(parents, child) {

    child.indiv.reset();

    let weights_ih = [];
    let weights_ho = [];
    let bias_h = [];
    let bias_o = [];

    for (parent of parents) {
      weights_ih.push(parent.indiv.brain.weights_ih);
      weights_ho.push(parent.indiv.brain.weights_ho);
      bias_h.push(parent.indiv.brain.bias_h);
      bias_o.push(parent.indiv.brain.bias_o);
    }

    child.indiv.brain.weights_ih = Matrix.mix(weights_ih);
    child.indiv.brain.weights_ho = Matrix.mix(weights_ho);
    child.indiv.brain.bias_h = Matrix.mix(bias_h);
    child.indiv.brain.bias_o = Matrix.mix(bias_o);

    return child;
  }

  mutate(population) {
    for (let individu of population) {
      individu.indiv.brain.mutate((x,i,j)=>{if (Math.random()<0.01) {return x+randomGaussian() * 0.5;} else{return x}});
    }
    return population;
  }

  pickone(popul) {
    //get the total fitness
    let totalfitness = 0;
    for (let individu of popul) {
      let thefitness = individu.indiv.score;
      totalfitness+=thefitness;
    }

    //get the normalized fitness
    for (let individu of popul) {
      let thenfitness = individu.indiv.score/totalfitness;
      individu.nfit = thenfitness;
    }

    //tri par ordre décroissant des fitness normalized
    popul.sort((a,b)=>b.nfit-a.nfit);

    //accumulated fitness calculation
    let accumulatedfit = 0;
    for (let individu of popul) {
      accumulatedfit += individu.nfit;
      individu.accnfit = accumulatedfit;
    }

    //end of selection
    let r = Math.random();
    let thechosenone = undefined;
    let index = 0;
    do {
      thechosenone = popul[index];
      index++;
    } while(thechosenone.accnfit < r)


    //add thechosenone to the list of survivors
    popul.splice(index-1,1);

    return thechosenone;


  }
}

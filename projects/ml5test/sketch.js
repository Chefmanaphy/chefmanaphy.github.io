const model = tf.sequential();

let anyfunction = ((x) => {
	return Math.sin(x);
});

nums = (function () {
	let res = [];for (let i=0;i<2*Math.PI;i+=0.01) {res.push(i);}return res;
}());

let xs = tf.tensor2d(nums,[nums.length,1]);

let ys = tf.tensor2d((function(thefunction) {
	let res=[];for (let i of nums) {res.push(thefunction(i));}return res;
}(anyfunction)),[nums.length,1])

model.add(tf.layers.dense({units:1, inputShape:[1]}));

model.compile({optimizer: 'sgd', loss: 'meanSquaredError'});


// model.fit(xs, ys, {epochs: 1000});

// model.predict(tf.tensor2d([[3.14]],[1,1])).print();

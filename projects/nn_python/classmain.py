import numpy as np

def sigmoid(x):
	return(1/(1+np.exp(-x)))

def derivatives_sigmoid(x):
	return(x*(1-x))

class Neuralnet:
	def __init__(self,shape):
		self.shape = shape
		self.layers = []
		self.layers.append(Layer(self,shape[0]))
		for i in range(len(shape)-1):
			self.layers.append(Layer(self,shape[i+1],self.layers[i]))
	def train(self,input, y, epoch):
		for i in range(epoch):
			self.forewardprop(input)
			self.backwardprop(y)
			if (i%int(epoch/100) == 0):
				print(str(int((i/epoch)*100))+"%")
		print("100%")
		print(self.layers[-1].values)


	def forewardprop(self,input):
		self.layers[0].setInput(input)
		for i in range(1,len(self.layers)):
			self.layers[i].execute(input)
		return(self.layers[-1].values)

	def backwardprop(self,y):
		for i in range(len(self.layers)-1,0,-1):
			if (i == len(self.layers)-1):
				E = y-self.layers[i].values
			else:
				E = self.layers[i+1].delta.dot(self.layers[i+1].weights.T)
			self.layers[i].update(E)
		for i in range(len(self.layers)-1,0,-1):
			self.layers[i].update2()

class Layer:
	def __init__(self,nn,neurons,prevlayer = None):
		self.nn = nn
		self.neurons = neurons
		self.prevlayer = prevlayer
		self.values = None
		if (prevlayer != None):
			self.weights = np.random.uniform(size = (prevlayer.neurons,neurons))
			self.bias = np.random.uniform(1,neurons)
			print(self.weights.shape)
	def setInput(self,input):
		if (self.prevlayer == None):
			self.values = input
	def execute(self,input):
		if (self.prevlayer != None):
			self.values = np.dot(self.prevlayer.values,self.weights)
		else:
			self.values = np.dot(input,self.weights)
		self.values+= self.bias
		self.values = sigmoid(self.values)
	def update(self,E):
		self.E = E
		self.slope = derivatives_sigmoid(self.values)
		self.delta = E*self.slope
		self.bias+=np.sum(self.delta,axis=0,keepdims=True)
	def update2(self):
		self.weights+=self.prevlayer.values.T.dot(self.delta)

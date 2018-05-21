import numpy as np
import classmain

def main():
	nn = Neuralnet([4,4,1])
	input = np.array([[0,0,0,0],[0,1,0,0],[1,0,0,0],[1,1,0,0]])
	output = np.array([[1],[0],[0],[1]])
	nn.train(input,output,200000)
	print(nn.forewardprop([[1,0,0,0]]))


if __name__ == "__main__":
	main()

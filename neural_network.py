# neural_network.py
import numpy as np

class NeuralNetwork:
    def __init__(self, input_nodes=13, hidden_nodes=16, output_nodes=4, weights=None):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        #Normalisation des poids pour stabiliser apprentissage
        self.weights_input_hidden = np.random.randn(input_nodes, hidden_nodes) * 0.5
        self.weights_hidden_output = np.random.randn(hidden_nodes, output_nodes) * 0.5


        if weights is None:
            self.weights_input_hidden = np.random.randn(input_nodes, hidden_nodes)
            self.weights_hidden_output = np.random.randn(hidden_nodes, output_nodes)
        else:
            self.weights_input_hidden, self.weights_hidden_output = weights

    def relu(self, x):
        return np.maximum(0, x)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def softmax(self, x):
        e = np.exp(x - np.max(x))
        return e / np.sum(e)


    def forward(self, inputs):
        inputs = np.array(inputs).reshape(-1, 1)
        hidden = self.relu(self.weights_input_hidden.T @ inputs)
        output = self.weights_hidden_output.T @ hidden
        return self.softmax(output).flatten()


    def get_weights(self):
        return [self.weights_input_hidden.copy(), self.weights_hidden_output.copy()]


    # mutation par ajout de bruit gaussien pour mutation moins brutale
    def mutate(self, rate=0.05, scale=0.1):
        for w in [self.weights_input_hidden, self.weights_hidden_output]:
            mask = np.random.random(w.shape) < rate
            w[mask] += np.random.randn(*w[mask].shape) * scale

    @staticmethod
    def crossover(p1, p2):
        w1 = p1.get_weights()
        w2 = p2.get_weights()
        child = []
        for a, b in zip(w1, w2):
            mask = np.random.rand(*a.shape) > 0.5
            child.append(np.where(mask, a, b))
        return NeuralNetwork(weights=child)

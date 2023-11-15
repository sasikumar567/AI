import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Initialize weights and biases
        self.weights_input_hidden = np.random.rand(self.input_size, self.hidden_size)
        self.biases_hidden = np.random.rand(1, self.hidden_size)
        self.weights_hidden_output = np.random.rand(self.hidden_size, self.output_size)
        self.biases_output = np.random.rand(1, self.output_size)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def feedforward(self, inputs):
        self.hidden_sum = np.dot(inputs, self.weights_input_hidden) + self.biases_hidden
        self.hidden_output = self.sigmoid(self.hidden_sum)
        self.output_sum = np.dot(self.hidden_output, self.weights_hidden_output) + self.biases_output
        self.predicted_output = self.sigmoid(self.output_sum)
        return self.predicted_output

    def backward(self, inputs, targets, learning_rate):
        output_errors = targets - self.predicted_output
        output_delta = output_errors * self.sigmoid_derivative(self.predicted_output)

        hidden_errors = output_delta.dot(self.weights_hidden_output.T)
        hidden_delta = hidden_errors * self.sigmoid_derivative(self.hidden_output)

        self.weights_hidden_output += self.hidden_output.T.dot(output_delta) * learning_rate
        self.biases_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
        self.weights_input_hidden += inputs.T.dot(hidden_delta) * learning_rate
        self.biases_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate

    def train(self, inputs, targets, learning_rate, epochs):
        for epoch in range(epochs):
            self.feedforward(inputs)
            self.backward(inputs, targets, learning_rate)

    def predict(self, inputs):
        return self.feedforward(inputs)

# Example usage:
if __name__ == '__main__':
    # Sample dataset (XOR)
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    targets = np.array([[0], [1], [1], [0]])

    # Create a neural network with 2 input nodes, 4 hidden nodes, and 1 output node
    neural_network = NeuralNetwork(2, 4, 1)

    # Train the neural network
    neural_network.train(inputs, targets, learning_rate=0.1, epochs=10000)

    # Make predictions
    predictions = neural_network.predict(inputs)
    print("Predictions:")
    print(predictions)

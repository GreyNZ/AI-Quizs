def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""
    def perceptron(input):
        # Complete (a line or two)
        result = 0
        for i in range(0, len(input)):
            result += (weights[i] * input[i])
        # Note: we are masking the built-in input function but that is
        # fine since this only happens in the scope of this function and the
        # built-in input is not needed here.
        if result + bias < 0:
            return 0
        else:
            return 1
    return perceptron # this line is fine


def accuracy(classifier, inputs, expected_outputs):
    accuracy = 1
    for i in range(0, len(inputs)):
        classified_value = classifier(inputs[i])
        if classified_value != expected_outputs[i]:
            accuracy -= (1 / len(inputs))
    return accuracy


perceptron = construct_perceptron([-1, 3], 2)
inputs = [[1, -1], [2, 1], [3, 1], [-1, -1]]
targets = [0, 1, 1, 0]

print(accuracy(perceptron, inputs, targets))

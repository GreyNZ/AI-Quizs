def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""

    def perceptron(input):
        result = 0
        for i in range(0, len(input)):
            result += (weights[i] * input[i])
        # Note: we are masking the built-in input function but that is
        # fine since this only happens in the scope of this function and the
        # built-in input is not needed here.
        result += bias
        if result >= 0:
            return 1
        else:
            return 0
    return perceptron


# weights = [2, -4]
# bias = 0
# perceptron = construct_perceptron(weights, bias)
#
# print(perceptron([1, 1]))
# print(perceptron([2, 1]))
# print(perceptron([3, 1]))
# print(perceptron([-1, -1]))
#
# weights = [3, 5]
# bias = 1
# perceptron = construct_perceptron(weights, bias)
#
# print(perceptron([0, 0]))
# print(perceptron([1, -1]))
# print(perceptron([-1, 1]))

def accuracy(classifier, inputs, expected_outputs):
    """Passes each input in the sequence of inputs to the given classifier function (e.g. a perceptron) and compares the
     predictions with the expected outputs. Returns the accuracy of the classifier on the given data.
     Accuracy is a number between 0 and 1 (inclusive)."""
    result = 1

    for i in range(0, len(inputs)):
        classifier_result = classifier(inputs[i])
        if classifier_result != expected_outputs[i]:
            result -= (1 / len(inputs))

    return result


perceptron = construct_perceptron([-1, 3], 2)
inputs = [[1, -1], [2, 1], [3, 1], [-1, -1]]
targets = [0, 1, 1, 0]

print(accuracy(perceptron, inputs, targets))

import math


def euclidean_distance(v1, v2):
    """Returns the euclidean distance between the points represented by v1 and v2."""
    result = 0
    for i in range(0, len(v1)):
        result += (v1[i] - v2[i]) ** 2

    return math.sqrt(result)


# print(euclidean_distance([0, 3, 1, -3, 4.5], [-2.1, 1, 8, 1, 1]))


def majority_element(labels):
    """Returns the label that has the highest frequency"""
    return max(set(labels), key=labels.count)


# print(majority_element([0, 0, 0, 0, 0, 1, 1, 1]))
# print(majority_element("ababc") in "ab")


def knn_predict(input, examples, distance, combine, k):
    """Takes an input and predicts the output by combining the output of the k nearest neighbours."""
    k_neighbours = sorted(((distance(input, example[0]), example[1]) for example in examples), key=lambda x: x[0])

    chosen, k_neighbours = k_neighbours[:k], k_neighbours[k:]

    for i in k_neighbours:
        if i[0] == chosen[-1][0]: chosen.append(i)

    return combine([i[1] for i in chosen])


# examples = [
#     ([2], '-'),
#     ([3], '-'),
#     ([5], '+'),
#     ([8], '+'),
#     ([9], '+'),
# ]
#
# distance = euclidean_distance
# combine = majority_element
#
# for k in range(1, 6, 2):
#     print("k =", k)
#     print("x", "prediction")
#     for x in range(0, 10):
#         print(x, knn_predict([x], examples, distance, combine, k))
#     print()
#
# examples = [
#     ([1], 5),
#     ([2], -1),
#     ([5], 1),
#     ([7], 4),
#     ([9], 8),
# ]
#
#
# def average(values):
#     return sum(values) / len(values)
#
#
# distance = euclidean_distance
# combine = average
#
# for k in range(1, 6, 2):
#     print("k =", k)
#     print("x", "prediction")
#     for x in range(0, 10):
#         print("{} {:4.2f}".format(x, knn_predict([x], examples, distance, combine, k)))
#     print()

import math
import numpy as np


x = np.array([4, 3, 0])
c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])


def sigmoid(z):
    # add your implementation of the sigmoid function here
    sigmoid_result = 1 / (1 + math.exp(-z))
    print(f"sigmoid_result: {sigmoid_result}")

    return sigmoid_result

# calculate the output of the sigmoid for x with all three coefficients
coeff_list = [c1, c2, c3]
results = []

for coeff in coeff_list:
    z = sum(x[i] * coeff[i] for i in range(len(x)))
    sigm_result = sigmoid(z)
    results.append(sigm_result)

# another way
'''
for coeff in coeff_list:
    z = np.dot(x, coeff)
    sigm_result = sigmoid(z)
    results.append(sigm_result)
'''

max_sigmoid = max(results)
print(f"Max sigmoid results is: {max_sigmoid}")

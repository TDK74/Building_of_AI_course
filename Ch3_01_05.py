#import numpy as np


# input values for three mökkis: 
#  - size [m^2], 
#  - size of the sauna [m^2], 
#  - distance to water [m], 
#  - number of indoor bathrooms, 
#  - proximity of neighbors [m]
X = [[66, 5, 15, 2, 500], 
    [21, 3, 50, 1, 100], 
    [120, 15, 5, 2, 1200]]
#X = np.array([[66, 5, 15, 2, 500],
#            [21, 3, 50, 1, 100], 
#            [120, 15, 5, 2, 1200]])


# coefficient values
c = [3000, 200 , -50, 5000, 100]
#c = np.array([3000, 200 , -50, 5000, 100])

def predict(X, c):
    # write a loop that goes over the cabin data and for each cabin prints out 
    # the predicted price of the cabin you can assume that the number of inputs
    # and the number of coefficients are the same

    for x in X:
        price = c[0]*x[0] + c[1]*x[1] + c[2]*x[2] + c[3]*x[3] + c[4]*x[4]
        print(price)

    #for x_row in X:
    #    price = sum([x_row[idx] * c[idx] for idx in range(len(x_row))])
    #    print(price)

    #for x_row in X:
    #    price = sum([x * coef for x, coef in zip(x_row, c)])
    #    print(price)

    #print(X @ c)   # works with numpy arrays of X and c


predict(X, c)

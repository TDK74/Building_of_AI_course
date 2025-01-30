import numpy as np


# input values for three mökkis: size, size of sauna, distance to water, number of indoor bathrooms, 
# proximity of neighbors
X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]
c = [3000, 200, -50, 5000, 100]    # coefficient values

def predict(X, c):
    # with np arrays
    #x = np.array(X)
    #coef = np.array(c)
    #price = x @ coef

    # w/o np arrays
    #price = np.matmul(X, c)
    price = np.dot(X, c)
    
    #print('\n'.join(str(p) for p in price))
    for p in price:
        print(p)

predict(X, c)

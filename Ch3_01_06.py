import numpy as np


X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])
c = np.array([3000, 200 , -50, 5000, 100])    # coefficient values
 
def squared_error(X, y, c):
    sse = 0.0

    for xi, yi in zip(X, y):
        # add your code here: calculate the predicted price,
        # subtract it from the actual price yi, 
        # square the difference using (yi - prediction)**2, 
        # and add up all the differences in variable sse
        
        # Calculate the predicted price
        prediction = sum([x * coef for x, coef in zip(xi, c)])
        #prediction = X @ c                 # with np arrays

        # Subtract the predicted price from the actual price,
        # square the difference, and add it to SSE
        sse += ((yi - prediction) ** 2)
        #sse = sum((y - prediction) ** 2)   # with np arrays
        
        #pass

    print(sse)

squared_error(X, y, c)

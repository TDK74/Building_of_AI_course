import numpy as np


# data
X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([[3000, 200 , -50, 5000, 100], 
              [2000, -250, -100, 150, 250], 
              [3000, -100, -150, 0, 150]])   

def find_best(X, y, c):
    smallest_error = np.Inf
    best_index = -1
    sse = 0.0
    idx = 0

    for coeff in c:
        #pass   # edit here: calculate the sum of squared error with coefficient set coeff and
                # keep track of the one yielding the smallest squared error
        errors = y - (X @ coeff)    # calculate the errors
        sse = np.sum(errors ** 2)   # sum of squared errors

        # update the smallest_error and the best_index if necessary
        if sse < smallest_error:
            smallest_error = sse
            best_index = idx
        
        idx += 1
        
    print("the best set is set %d" % best_index)


find_best(X, y, c)

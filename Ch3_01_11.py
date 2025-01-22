import numpy as np
from io import StringIO


input_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
 
def fit_model(input_file):
    # Please write your code inside this function

    # print the content of input_file
    #print(input_file.getvalue())

    # read the imput_string/file into a np array
    string_data = np.genfromtxt(input_file, delimiter=' ')

    # separate X and y
    X = string_data[ : , : -1]
    y = string_data[ : , -1]

    # print X and y to verify
    #print("X: ")
    #print(X)
    #print("\n y: ")
    #print(y)

    # calculate coefficients
    #coeff = np.linalg.pinv(X).dot(y)
    #coeff, residuals, rank, singular_values = np.linalg.lstsq(X, y, rcond=None)
    coeff = np.linalg.lstsq(X, y)[0]
    
    # print coefficients to verify
    #print("\n Coefficients: ")
    #print(coeff)

    # also possible for the final calculations and to avoid the next lines (48 to 53)
    #print(coeff)
    #print(X @ coeff)

    # read the data in and fit it. the values below are placeholder values
    c = np.asarray(coeff)  # coefficients of the linear regression
    x = np.asarray(X)  # input data to the linear regression

    print(c)
    print(x @ c)

# simulate reading a file
input_file = StringIO(input_string)
fit_model(input_file)

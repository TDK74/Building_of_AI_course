portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# https://sea-distances.org/
# nautical miles converted to km

D = [
        [0,8943,8019,3652,10545],
        [8943,0,2619,6317,2078],
        [8019,2619,0,5836,4939],
        [3652,6317,5836,0,7825],
        [10545,2078,4939,7825,0]
    ]

# https://timeforchange.org/co2-emissions-shipping-goods
# assume 20g per km per metric ton (of pineapples)

co2 = 0.020

# DATA BLOCK ENDS

# these variables are initialised to nonsensical values
# your program should determine the correct values for them
smallest = 1000000
bestroute = [0, 0, 0, 0, 0]

def permutations(route, ports):
    # write the recursive function here
    # remember to calculate the emissions of the route as the recursion ends
    # and keep track of the route with the lowest emissions
    # pass
    if len(ports) < 1:
        if route[0] == 0:
            yield route
    else:
        for idx in range(len(ports)):
            yield from permutations(route + [ports[idx]], ports[ : idx] + ports[idx + 1: ])


def calculate_emissions(route):
    distance = sum(D[route[i]][route[i + 1]] for i in range(len(route) - 1))
    emissions = distance * co2

    return emissions


def main(smallest=1000, bestroute=None):    # default values not to mess up the testing
    # Do not edit any (global) variables using this function, as it will mess up the testing
    if bestroute is None:
        bestroute = []

    # this will start the recursion 
    for route in permutations([0], list(range(1, len(portnames)))):
        emissions = calculate_emissions(route)

        if emissions < smallest:
            smallest = emissions
            bestroute = route

    # print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

main(smallest, bestroute)

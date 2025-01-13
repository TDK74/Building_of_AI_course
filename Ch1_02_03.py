def permutations(route, ports):
    if len(ports) < 1:
        if route[0] == 0:   # this check is better here to avoid generation of all possible permutations
            yield route
    else:
        for i in range(len(ports)):
            yield from permutations(route + [ports[i]], ports[ :i] + ports[i+1: ])

def main():
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

    for route in permutations([], [0, 1, 2, 3, 4]):
        #if route[0] == 0:
            distance = sum(D[route[i]][route[i+1]] for i in range(len(route) - 1)) 
            #distance = D[route[0]][route[1]] + D[route[1]][route[2]] + D[route[2]][route[3]] + D[route[3]][route[4]]
            emissions = distance * co2
            print(' '.join([portnames[i] for i in route]) + " %.1f kg" % emissions)
    
main()

import numpy as np
#import random


def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    
    #seq = random.choices([0, 1], weights = [1 - p1, p1], k = 10000)    # working
    seq = np.random.choice([0, 1], p = [1 - p1, p1], size = 10000)
    
    return seq

def count(seq):
    # insert code to return the number of occurrences of 11111 in the sequence
    positions = []
    consec = 5
    ones = [1] * consec
    #ones = np.array([1] * consec)      # working
    counter = 0

    for idx in range(len(seq) - consec + 1):
        #if all(seq[idx + i] == 1 for i in range(consec)):          # working, no need of ones
        #if all(elem == 1 for elem in seq[idx : idx + consec]):     # working, no need of ones
        if all(seq[idx : idx + consec] == ones):                    # working
        #if np.array_equal(seq[idx : idx + consec], ones):          # working
            counter += 1
            positions.append(idx)
    
    #print(f"Positions of occurences of 11111 are: {positions}")

    return counter

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))

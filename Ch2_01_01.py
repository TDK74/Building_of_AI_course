def count11(seq):
# define this function and return the number of occurrences as a number
    counter = 0
    
    for idx in range(len(seq) - 1):
        if seq[idx] == 1 and seq[idx + 1] == 1:
            counter += 1

    return counter

print(count11([0, 0, 1, 1, 1, 0])) # this should print 2

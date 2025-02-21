import random

def accept_prob(S_old, S_new, T):
    # this is the acceptance "probability" in the greedy hill-climbing method
    # where new solutions are accepted if and only if they are better
    # than the old one.
    # change it to be the acceptance probability in simulated annealing

    if S_new > S_old:
        return 1.0
    elif T > 0: # to avoid ZeroDivisionError
        return math.exp( -(S_old - S_new) / T)
    else:   # to test when T = 0
        return 0.0

# the above function will be used as follows. this is shown just for
# your information; you don't have to change anything here
def accept(S_old, S_new, T):
    if random.random() < accept_prob(S_old, S_new, T):
        print(True)
    else:
        print(False)

S_old = 150
S_new = 140

for T in range(50):
    accept(S_old, S_new, T)

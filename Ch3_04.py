import random

def main():

    rdm = random.random()
    # print(rdm)

    if rdm < 0.8:           # 80% for dogs
        favourite = "dogs"
    elif rdm < 0.9:         # next 10% for cats
        favourite = "cats"
    else:                   # last 10% for bats
        favourite = "bats"  # change this
    print("I love " + favourite) 

main()

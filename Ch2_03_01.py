def flip(n):
    odds = 1.0  # start with 50% chance of the magic coin, which is the same as odds = 1:1
    r = 2.0     # r = P(heads | magic) / P(heads | normal) = 1 / 0.5 = 2
    odds = odds * (r ** n)
    #for i in range(n):
    #    odds *= r           # edit here to update the odds
    print(odds)

n = 3
flip(n)

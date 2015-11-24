def sieve(num):
    
    fullset = set(range(2, num))
    base = set([2,3,5,7])
    twos = set([x for x in fullset if x % 2 == 0])
    threes = set([x for x in fullset if x % 3 == 0])
    fives = set([x for x in fullset if x % 5 == 0])
    sevens = set([x for x in fullset if x % 7 == 0])
    
    difference = base | fullset - twos - threes - fives - sevens

    return difference

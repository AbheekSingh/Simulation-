import random

def exploreOnly():
    happiness = 0
    attempts = 300
    while attempts > 0:
        # cafeteria 1
        happiness = happiness + random.normalvariate(9, 3)
        attempts -= 1
        # cafeteria 2
        happiness = happiness + random.normalvariate(7, 5)
        attempts -= 1
        # cafeteria 3
        happiness = happiness + random.normalvariate(11, 7)
        attempts -= 1
    return happiness
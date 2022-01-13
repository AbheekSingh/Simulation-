import random


def e_greedy(e: int):
    c1_count = 1
    c2_count = 1
    c3_count = 1
    # go to each cafeteria once and save the happiness score
    c1 = random.normalvariate(9, 3)
    c2 = random.normalvariate(7, 5)
    c3 = random.normalvariate(11, 7)
    # calculate average by dividing all collective happiness scores by # of visits to the cafeteria
    for day in range(297):  # how to run t trials for overall code?
        c1avg = c1 // c1_count
        c2avg = c2 // c2_count
        c3avg = c3 // c2_count
        r = 100 * random.random()  # random float b/w 0 and 1 to compare to e
        if r < e:
            c = random.randint(1, 3)  # choose random cafeteria 1, 2 or 3
            if c == 1:  # cafeteria 1
                c1 += random.normalvariate(9, 3)
                c1_count += 1
            elif c == 2:  # cafeteria 2
                c2 += random.normalvariate(7, 5)
                c2_count += 1
            else:  # cafeteria 3
                c3 += random.normalvariate(11, 7)
                c3_count += 1
        elif r >= e:  # pick best cafeteria so far
            if max(c1avg, c2avg, c3avg) == c1avg:  # cafeteria 1
                c1 += random.normalvariate(9, 3)
            elif max(c1avg, c2avg, c3avg) == c2avg:  # cafeteria 2
                c2 += random.normalvariate(7, 5)
            else:  # cafeteria 3
                c3 += random.normalvariate(11, 7)
    sum = c1 + c2 + c3
    return sum

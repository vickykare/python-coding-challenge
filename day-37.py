"""
This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.

"""


import math


def printPowerSet(set, set_size):

    Newset = []
    pow_set_size = (int)(math.pow(2, set_size))
    # print(pow_set_size)

    for counter in range(0, pow_set_size):

        tempSet = []

        for j in range(0, set_size):
            if((counter & (1 << j)) > 0):
                tempSet.append(set[j])
                # print(set[j], end="")
        Newset.append(tempSet)
    print(Newset)  


if __name__ == "__main__":
        
    set = [1, 2, 3]
    printPowerSet(set, len(set))
# Chapter1 - Q1

'''
# O(n^2)
def permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    #return all(string1.count(s) == string2.count(s) for s in set(string1))
    if len(set(string1)) != len(set(string2)):
        return False
    for s in set(string1):
        if string1.count(s) != string2.count(s):
            return False
    return True
'''

from collections import Counter
# O(n)
def permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    c = Counter()
    for s in string1:
        c[s] += 1
    for s in string2:
        if not c[s]:
            return False
        c[s] -= 1
    return True    

# test case 1
input1 = "cat"
input2 = "act"
print("{} is a permutation of {} --> {}".format(input1, input2, permutation(input1, input2)))

# test case 2
input1 = "area"
input2 = "era"
print("{} is a permutation of {} --> {}".format(input1, input2, permutation(input1, input2)))

# test case 3
input1 = "God"
input2 = "dog"
print("{} is a permutation of {} --> {}".format(input1, input2, permutation(input1, input2)))

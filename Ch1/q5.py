# Chapter1 - Q5: One Away

from collections import Counter

def oneaway(s, t):
    if abs(len(s) - len(t)) > 1:
        return False
    if len(s) == len(t):
        return replace_edit(s,t)
    if len(s) == len(t) + 1:
        return remove_edit(s,t)
    if len(s) + 1 == len(t):
        return remove_edit(t,s)

def replace_edit(s, t):
    num_away = 0
    for item in zip(s,t):
        if item[0] != item[1]:
            if num_away:
                return False
            num_away += 1
    return True
           
def remove_edit(s,t):
    counter = Counter()
    for c in s:
        counter[c] += 1
    for c in t:
        counter[c] -= 1
    return sum(counter.values()) == 1

# test case 1
s1 = "pale"
t1 = "ple"
print(oneaway(s1, t1))

# test case 2
s2 = "pales"
t2 = "pale"
print(oneaway(s2, t2))

# test case 3
s3 = "pale"
t3 = "bale"
print(oneaway(s3, t3))

# test case 4
s4 = "pale"
t4 = "bake"
print(oneaway(s4, t4))

# test case 5
s5 = "ple"
t5 = "pale"
print(oneaway(s5, t5))

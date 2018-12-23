# Chapter1 - Q4: Palindrome Permutation

from collections import Counter
import numpy as np

# O(n) time
# O(n) space (i.e. hashmap)

def PalindromePerm(string):
    string = string.lower().replace(" ", "")
    c = Counter()
    for s in string:
        c[s] += 1
    cnt_total = 0    
    for s in c:
        cnt_total += c[s] % 2
        if cnt_total > 1:
            return False

input1 = "Tact Coa"
print(PalindromePerm(input1))

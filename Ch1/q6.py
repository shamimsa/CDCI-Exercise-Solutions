# Chapter1 - Q5: One Away

from collections import OrderedDict

def compress(s):
    cnt = 1
    s_comp = ""
    for i in range(1,len(s)):
        if s[i-1] != s[i]:
            print("%s discovered %i times" % (s[i-1], cnt))
            s_comp = s_comp + s[i-1] + str(cnt)         
            cnt = 1
        cnt += 1
    if len(s_comp) < len(s):
        return s_comp
    return s

input1 = "aabcccccaaa"
print(compress(input1))


# Chapter1 - Q1
def is_unique(my_str):
    # there are 128 ASCII characters
    if len(my_str) > 128:
        return False

    chars = [False for _ in range(128)]
    for s in my_str:
        val = ord(s)
        if chars[val]:
            return False
        chars[val] = True
    return True

str_test = 'united %^^)(*'
print(is_unique(str_test))

# Chapter1 - Q3: urlify

def URLify(string, length):
    return string[:length].replace(' ', '%20')

input1 = "Mr John Smith    "
print(URLify(input1,13))

input2 = "Name:  Shamim Samadi      "
print(URLify(input2,20))

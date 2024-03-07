def CountLetters(s):
    upper = 0
    lower = 0
    for x in s:
        if x.isupper():
            upper +=1
        else:
            lower += 1
    return upper, lower

s = input()
print(CountLetters(s))
def capitalize(word):
    first = chr(ord(word[0]) - 32)
    return first + word[1:]

source = input().split()
res = []
for word in source:
    res.append(capitalize(word))
print(' '.join(res))
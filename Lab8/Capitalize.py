def capitalize(word):
    first = word[0]
    first = chr(ord(first) - 32)
    return first + word[1:]

source = input().split()
res = []
for word in source:
    res.append(capitalize(word))
print(' '.join(res))
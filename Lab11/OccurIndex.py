words = [i for i in input().split()]
occurs = dict()
for word in words:
    if word in occurs:
        occurs[word]+=1
    else:
        occurs[word] = 0
    print(occurs[word], end = ' ')
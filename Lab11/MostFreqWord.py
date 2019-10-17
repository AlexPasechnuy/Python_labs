num = int(input())
a = dict()
for i in range(num):
    words = input().split()
    for word in words:
        if word in a:
            a[word] += 1
        else:
            a[word] = 1

max_count = max(a.values())
most_frequent = [k for k, v in a.items() if v == max_count]
print(min(most_frequent))
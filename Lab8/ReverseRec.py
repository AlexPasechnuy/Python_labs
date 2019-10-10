def rev():
    a = int(input())
    if a!=0:
        rev()
    print(a)

rev()
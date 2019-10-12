students = [{input() for j in range(int(input()))} for i in range(int(input()))]
print(len(set.intersection(students)), *sorted(set.intersection(students)), sep='\n')
print(len(set.union(students)), *sorted(set.union(students)), sep='\n')
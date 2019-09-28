minutes = int(input())
hours = int((minutes/60)%24)
minutes = minutes%60
print(hours, minutes)
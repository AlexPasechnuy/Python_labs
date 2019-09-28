a = int(input())
minutes = int((a*45) + ((a - (a%2))*10) - (15 * ((a+1)%2)))
hours = 9 + minutes//60
minutes %= 60
print("%d %d" % (hours, minutes))
x1 = int(input())
x2 = int(input())
x3 = int(input())
y1 = int(input())
y2 = int(input())
y3 = int(input())
hourx = x1 * 60 * 60
minutex = x2 * 60
houry = y1 * 60 * 60
minutey = y2 * 60
print((houry + minutey + y3) - (hourx + minutex + x3))

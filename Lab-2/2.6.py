
a = int(input())
b = int(input())
c = int(input())


average = (a + b + c - min(a, b, c) - max(a, b, c))


print(average)

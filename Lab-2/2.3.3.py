a = int(input())
b = int(input())
c = int(input())


if a + b > c and a + c > b and b + c > a:
    
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or a == c or b == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Versatile"
else:
    triangle_type = "Not a triangle"


print(triangle_type)

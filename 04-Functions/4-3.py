###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
def triangle_area(a,b,c):
    s=(a+b+c)/2
    pole = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return pole

bok_a,bok_b,bok_c = 2,3,4

wynik=triangle_area(bok_a,bok_b,bok_c)
print(f'The area of ​​a triangle with sides {bok_c},{bok_b},{bok_c} is {wynik}')

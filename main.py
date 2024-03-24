import math

bok_a = 10.4

def square_area(a):
    return math.pow(a, 2)

print(square_area(bok_a))

# Pole prostokata
def triangle_area(a, h):
    return 0.5 * a * h

bok_a = 3
bok_b = 7

print(triangle_area(bok_a, bok_b))

# Pole trapezu
def trapezoid_area(a, b, h):
    return 0.5 * (a + b) * h

bok_a, bok_b, h, = 5, 10, 15

print(trapezoid_area(bok_a, bok_b, h))

# Pole kola
def circle_area(r):
    return math.pi * math.pow(r, 2)

promien = 10

print(circle_area(promien))


# To do:
# Moodle - swoje konto na githubie 
# Trzeba miec historie zmian! 
# Bedziemy wrzucac screenshoty commitow na github jako potwierdzenie ze cos tam robilismy 
# Do konca semestru trzymac historie commitow!

# Mozna bawic sie historia gita, manipulowac ja itp.
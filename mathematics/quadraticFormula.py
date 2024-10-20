import math, latexify
@latexify.function

def quadratic_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return root1, root2

quadratic_roots
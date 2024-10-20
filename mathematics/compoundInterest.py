import math, latexify
@latexify.function

def compound_interest(P, r, n, t):
    return P * (1 + r/n) ** (n * t)

compound_interest
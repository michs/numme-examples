# Newton's method.
#
# @return (x0, h, i) - zero,
#                      last improvement of the zero (error),
#                      number of iterations
#
def newton(x0, f, fprime, err, max_iter = 100):
    h = f(x0)/fprime(x0)
    x0 -= h
    i = 1
    while abs(h) > err and i < max_iter:
        h   = f(x0)/fprime(x0)
        x0 -= h
        i  += 1
    return (x0, h, i)
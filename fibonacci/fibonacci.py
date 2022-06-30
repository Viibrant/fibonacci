def fib(n: int):
    """lmao this is a fibonacci function you dumb dumb"""
    a, b = 1, 1
    for _ in range(n+1):
        yield a
        a, b = b, a + b
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n-1)


while True:
    try:
        a, b = map(int, input().split())
        print(fatorial(a) + fatorial(b))
    except EOFError:
        break
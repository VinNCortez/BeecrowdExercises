d = n = -1
while True:
    d, n = input().split()
    if d == '0' and n == '0':
        break
    resultado = n.replace(d, '')
    resultado = 0 if not resultado else int(resultado)
    print(resultado)
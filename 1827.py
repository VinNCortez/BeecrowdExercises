# Matriz Quadrada IV
import math
while True:
    try:
        size = int(input())
        one_third = size // 3
        mat = [[0] * size for i in range(size)]
        for x in range(size):
            for y in range(size):
                if x + 1 == math.ceil(size / 2) and y + 1 == math.ceil(size / 2):
                    mat[x][y] = 4
                elif one_third < x + 1 <= size - one_third and one_third < y + 1 <= size - one_third:
                    mat[x][y] = 1
                elif x == y:
                    mat[x][y] = 2
                elif x + y == size - 1:
                    mat[x][y] = 3
        result = "\n".join([(size * "{}").format(*mat[i]) for i in range(size)])
        print(result+"\n")
    except EOFError:
        break
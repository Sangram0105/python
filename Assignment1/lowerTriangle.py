def lower_triangular(n):
    for i in range(n):
        for j in range(i + 1):
            print('*', end=' ')
        print()

n = 5
lower_triangular(n)

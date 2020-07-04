user = int(input())


def eratosthenes(n):
    prime = []
    for i in range(2, n + 1):
        if i not in prime:
            print(i)
            for x in range(i * i, n + 1, i):
                prime.append(x)


eratosthenes(user)

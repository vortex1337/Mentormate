while True:
    n = int(input("N = "))
    j = 0
    m = 1
    for i in range((n + 1) // 2):
        print((n - i) * "-" + (n + j) * "*" + (n - j) * "-" + (n + j) * "*" + (n * 2 - j) * "-" + (n + j) * "*" + (n - j) * "-" + (n + j) * "*" + (n - i) * "-")
        j += 2
    for k in range(i, n):
        print((n - k - 1) * "-" + n * "*" + m * "-" + (2 * n - m)*"*" + m * "-" + n * "*" + (n - m) * "-" + n * "*" + m * "-" + (2 * n - m) * "*" + m * "-" + n * "*" + (n - k - 1) * "-")
        m += 2

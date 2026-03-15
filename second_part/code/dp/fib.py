def fib_bottom_up(n):
    if n <= 1:
        return n

    fib_numbers = [0] * (n + 1)

    fib_numbers[1] = 1

    for i in range(2, n + 1):
        fib_numbers[i] = fib_numbers[i - 1] + fib_numbers[i - 2]

    return fib_numbers[n]


def fib_top_down(n, memo=None):
    if not memo:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_top_down(n - 1, memo) + fib_top_down(n - 2, memo)
    return memo[n]


print(fib_bottom_up(9))
print(fib_top_down(9))

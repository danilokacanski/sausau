"""
Osoba se penje uz stepenice. U jednom skoku može da se
preskoči 1, 2 ili 3 stepenika. Napisati algoritam koji
određuje na koliko načina osoba može da pređe put koji
se sastoji od n stepenika.
"""


def climb_stairs_tab(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]


def climb_stairs_memo(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n == 0:
        return 1
    elif n < 0:
        return 0

    memo[n] = (
        climb_stairs_memo(n - 1, memo)
        + climb_stairs_memo(n - 2, memo)
        + climb_stairs_memo(n - 3, memo)
    )
    return memo[n]


print(climb_stairs_memo(5))
print(climb_stairs_tab(5))

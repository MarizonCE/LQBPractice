# 递推式：f(n) = f(n-1)*n + (n*(n-1))/2 * (n-1)!
MOD = 998244353


def main():
    n = int(input())
    f = [0] * (n + 1)
    f[1] = 0
    p = 1

    for i in range(1, n):
        p = p * i % MOD
        f[i + 1] = (i * (i + 1) // 2 % MOD * p % MOD + f[i] * (i + 1) % MOD) % MOD

    print(f[n])


if __name__ == "__main__":
    main()

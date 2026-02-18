def sieve(n) -> list[int]:
    """
    Returns a list of all prime numbers less than n
    using the sieve algorithm of Eratosthenes and sets.
    """
    if n <= 2:
        return []

    numbers = set(range(2, n))

    for i in range(2, int(n ** 0.5) + 1):
        if i in numbers:
            multiples = set(range(i * i, n, i))
            numbers -= multiples

    return numbers


def main() -> None:
    n: int = int(input())
    primes = sieve(n)
    print(*primes)


if __name__ == "__main__":
    main()

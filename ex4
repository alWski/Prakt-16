def cros(first, second, n) -> str:
    """
    Checks whether the number n belongs to the intersection
    of the sets first and second.

    Returns:
        'yes' — if the number is included in both sets.,
        'no' — otherwise.
    """
    if n in first.intersection(second):
        ans = 'yes'
    else:
        ans = 'no'
    return ans

def main() -> None:
    first = set(map(int, input().split()))
    second = set(map(int, input().split()))
    n = int(input())

    print(cros(first, second, n))

if __name__ == "__main__":
    main()

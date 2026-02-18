def dable(sp, n) -> str:
    """
    Checks whether the number n belongs to the set of repetitions.
    items in the sp list.

    Returns:
        'yes' — if the number occurs 2 or more times,
        'no' — otherwise.
    """
    start = set()
    dup = set()

    for x in sp:
        if x in start:
            dup.add(x)
        else:
            start.add(x)

    return 'yes' if n in dup else 'no'

def main() -> None:
    sp = list(map(int, input().split()))
    n = int(input())
    print(dable(sp, n))

if __name__ == "__main__":
    main()

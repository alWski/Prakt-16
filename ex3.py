def only_sweet_products(sweet, friend) -> int:
    """
    Returns the number of products,
    which only Sweet
    Tooth likes (none of his friends like).
    """
    only_sweet = sweet - friend
    return len(only_sweet)


def main() -> None:
    sweet = set(input().split())
    n = int(input())
    friend = set()
    for i in range(n):
        friend = friend.union(set(input().split()))
    print(only_sweet_products(sweet, friend))


if __name__ == "__main__":
    main()

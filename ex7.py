from itertools import permutations

def perm(nums) -> None:
    """
    Returns all permutations of the nums set
    in lexicographic order.
    """
    for p in permutations(nums):
        print(*p)

def main() -> None:
    nums = sorted(map(int, input().split()))

if __name__ == "__main__":
    main()

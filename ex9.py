from itertools import combinations

def podmn(nums, k) -> None:
    """
    Outputs all K-element subsets of a given set of nums.

    The combinations function from the itertools module is used.
    Each subset is output as a tuple.
    """
    for p in combinations(nums, k):
        print(p)

def main() -> None:
    nums = set(map(int, input().split()))
    k = int(input())
    podmn(nums, k)

if __name__ == "__main__":
    main()

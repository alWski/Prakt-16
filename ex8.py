from itertools import combinations

def podmn(nums) -> None:
    """
    Outputs all subsets of a given set of nums.

    The combinations function from the itertools module is used.
    Subsets are output as tuples.
    """
    for i in range(len(nums) + 1):
        for p in combinations(nums, i):
            print(p)

def main() -> None:
    nums = set(map(int, input().split()))
    podmn(nums)

if __name__ == "__main__":
    main()

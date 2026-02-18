def common_courses(n) -> int:
    """
    Returns the number of courses,
    which were chosen by all n students.
    """
    
    allk = set()
    for i in range(0, n):
        stud = set(input().split())
        allk = allk.union(stud)
    return len(allk)


def main() -> None:
    n = int(input())
    print(common_courses(n))


if __name__ == "__main__":
    main()

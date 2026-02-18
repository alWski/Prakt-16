def rebus_poisk() -> None:
    """
    Looking for rebus solutions: XOD+XOD+XOD=MAT.

    Method: we iterate over X, O, D (the numbers are different), we count MAT = 3 * XOD,
    then we check:
      - MAT is three-digit (100..999)
      - the numbers M,A,T are different
      - all 6 digits (X,O,D,M,A,T) are different
    Conclusion: XOD+XOD+XOD = MAT
    """
    for x in range(1, 10):
        for o in range(0, 10):
            for d in range(0, 10):
                if len({x, o, d}) == 3:
                    hod = 100 * x + 10 * o + d
                    mat = 3 * hod
                    mat_str = str(mat)
                    if (100 <= mat <= 999) and len({x, o, d, int(mat_str[0]), int(mat_str[1]), int(mat_str[2])}) == 6:
                        print(f"{hod}+{hod}+{hod}={mat}")


def main() -> None:
    rebus_poisk()


if __name__ == "__main__":
    main()

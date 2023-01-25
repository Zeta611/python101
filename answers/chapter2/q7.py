def check_parity(n):
    # 1은 2는 3은 4는 5는 6은 7은 8은 9는 X0은 (< 1E12)
    if n % 2 == 0:
        parity = "짝수"
    else:
        parity = "홀수"
    if n == 2 or n == 4 or n == 5 or n == 9:
        eun = "는"
    else:
        eun = "은"
    print(f"{n}{eun} {parity}입니다.")


check_parity(2)  # 2는 짝수입니다.
check_parity(101)  # 101은 홀수입니다.

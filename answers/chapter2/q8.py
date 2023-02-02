def navigate(direction):
    if direction == "w":
        print("전진")
    elif direction == "a":
        print("좌회전")
    elif direction == "s":
        print("후진")
    elif direction == "d":
        print("우회전")
    else:
        print("알 수 없는 명령입니다.")

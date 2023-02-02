def quadrant(x, y):
    if x > 0 and y > 0:
        return "제1사분면"
    elif x < 0 and y > 0:
        return "제2사분면"
    elif x < 0 and y < 0:
        return "제3사분면"
    elif x > 0 and y < 0:
        return "제4사분면"
    else:
        return "경계선"

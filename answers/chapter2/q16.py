def better(gold1, silver1, bronze1, gold2, silver2, bronze2):
    if gold1 > gold2:
        return "First"
    elif gold1 < gold2:
        return "Second"

    if silver1 > silver2:
        return "First"
    elif silver1 < silver2:
        return "Second"

    if bronze1 > bronze2:
        return "First"
    elif bronze1 < bronze2:
        return "Second"
    else:
        return "Tie"


print(better(10,4,24, 1,35,25))
print(better(1,35,25, 10,4,24))
print(better(10,18,0, 10,4,24))
print(better(10,4,24, 10,18,0))
print(better(10,20,5, 10,20,4))
print(better(10,20,4, 10,20,5))
print(better(10,20,5, 10,20,5))

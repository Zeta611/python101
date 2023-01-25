def rock_paper_scissors(a, b):
    if a == b:
        return "Tie"
    if a == "R" and b == "S" or a == "S" and b == "P" or a == "P" and b == "R":
        return "a"
    else:
        return "b"


print(rock_paper_scissors("R", "R"))  # Tie
print(rock_paper_scissors("R", "S"))  # a
print(rock_paper_scissors("R", "P"))  # b
print(rock_paper_scissors("S", "S"))  # Tie
print(rock_paper_scissors("S", "P"))  # a
print(rock_paper_scissors("S", "R"))  # b
print(rock_paper_scissors("P", "P"))  # Tie
print(rock_paper_scissors("P", "R"))  # a
print(rock_paper_scissors("P", "S"))  # b

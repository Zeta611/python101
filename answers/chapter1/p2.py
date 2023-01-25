alan = int(input("Alan: "))
john = int(input("John: "))
haskell = int(input("Haskell: "))
donald = int(input("Donald: "))
alonzo = int(input("Alonzo: "))
print("Favorite integers: ", alan, john, haskell, donald, alonzo)

alan_cp, john_cp, haskell_cp, donald_cp, alonzo_cp = (
    alan, john, haskell, donald, alonzo
)

alan += john_cp + alonzo_cp
john += alan_cp + haskell_cp
haskell += john_cp + donald_cp
donald += haskell_cp + alonzo_cp
alonzo += donald_cp + alan_cp

print("Final integers: ", alan, john, haskell, donald, alonzo)

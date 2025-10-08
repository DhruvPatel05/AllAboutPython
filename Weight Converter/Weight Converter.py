import math

weight = float(input("Weight: "))
is_inPound = input("(L)bs or (K)g: ")
if is_inPound == "L" or is_inPound == "l":
    weight = (weight * 0.45)
    print(f"You are {weight:.2f} kilos")
elif is_inPound == "K" or is_inPound == "k":
    weight = (weight * 2.2)
    print(f"You are {weight:.2f} pounds")
else:
    print("enter proper weight")

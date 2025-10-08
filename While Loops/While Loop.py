i = 1
while i <= 5:
    print('*'* i)
    i = i + 1
print("Done")

final_Number = 9
guess_count = 0
guess_limit = 3
while guess_count<guess_limit:
    guess_number = int(input("Guess:"))
    guess_count += 1
    if final_Number == guess_number:
        print("You won!")
        break
else:
    print('Sorry you failed')
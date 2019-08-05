yn = input("Continue? Yes or No: ")
yn = yn.lower()
if yn[0] == 'y':
    print("You typed 'Yes'.")
if yn[0] == 'n':
    print("You typed 'No'.")
elif yn == 'spam':
    print(yn, "and eggs.")
else:
    print("You entered an invalid value")

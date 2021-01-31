

number = input("Enter a number, and i'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nTHe number " + str(number) + " is even")
else:
    print("\nTHe number " + str(number) + " is odd")
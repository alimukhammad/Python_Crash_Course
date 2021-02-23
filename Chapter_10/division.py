

print("Give me two numbers and ill divide them")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("YOu'cant divide by 0!")
    else:
        print(answer)

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero")

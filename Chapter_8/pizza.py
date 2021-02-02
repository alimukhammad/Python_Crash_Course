

def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + "-inches pizza with the following toppings:")
    for i in toppings:
        print("- " + i)

# make_pizza(16, "pepperoni")
# make_pizza(14, "mushroom", "green pepper", "extra cheese")
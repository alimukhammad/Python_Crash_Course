

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print("you ordered a " + pizza['crust'] + " crust pizza " + "with the following toppings:")
for i in pizza['toppings']:
    print("\t + topping")
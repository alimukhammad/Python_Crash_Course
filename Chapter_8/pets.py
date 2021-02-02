

def describe_pet(animal_type, pet_name):
    # Display information about pet
    print("\nI have a " + animal_type)
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type="Gorilla", pet_name="Bill")


def describe_petts(animalType, petName = "Mill"):
    # Display information about pet
    print("\nI have a " + animalType)
    print("My " + animalType + "'s name is " + petName.title() + ".")

describe_pet("Bear", "tom")
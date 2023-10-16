name = input()

while name != "Welcome!":
    length = len(name)
    if length < 5:
        print(f"{name} goes to Gryffindor.")
    elif length == 5:
        print(f"{name} goes to Slytherin.")
    elif length == 6:
        print(f"{name} goes to Ravenclaw.")
    elif length > 6:
        print(f"{name} goes to Hufflepuff.")
    name = input()
if name == "Voldemort":
    print("You must not speak of that name!")
elif name == "Welcome!":
    print("Welcome to Hogwarts.")


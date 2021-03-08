def bond_a_name(first="James", last="Bond"):
    """
    Bond, James Bonde
    :param first: first name
    :param last: last name
    :return: last, first last
    """
    return f"{last}, {first} {last}"

def great(name):
    """
    print: the name is {name}
    :param name: the name to use
    :return: nothing
    """
    print(f"The name is: {name}")

print(bond_a_name("James", "Bond"))
print("Bogdan")

great(bond_a_name())
great(bond_a_name("Padi", "Brown"))
great("Brown, Padi Brown")
# these last ones are the same.

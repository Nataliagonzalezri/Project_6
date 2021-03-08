def dragon (heat, damage=10):
    # in damage=10, the 10 is the value by default.
    """
    Creates a mean dragon
    :param heat: potency of dragon fire (1-100)
    :param damage: how hard the dragon bites (1-50)
    :return:the sum of heat and damage
    """
    try:
        heat = int(heat)
        damage = int(damage)
    except ValueError:
        print("You must use numbers for the dragon attributes")
        return
    # return means stop the function here. We use it when it is not a loop.
    # here comes the body of the function
    print(f"you are creating a dragon with a fire power of {heat} and bite power of {damage}")
    return heat+damage

dragon1 = dragon(7, 10)
dragon2 = dragon(damage=17, heat=45)
if dragon1 > dragon2:
    print("Dragon1 is stronger")
else:
    print("Dragon2 is stronger")


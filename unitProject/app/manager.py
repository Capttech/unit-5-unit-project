import random


# ==========| GENERATE USER ID |==========#
def generateUserId():
    list1 = [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
    ]
    return f"{random.choice(list1)}{random.choice(list1)}{random.choice(list1)}{random.choice(list1)}{random.choice(list1)}"

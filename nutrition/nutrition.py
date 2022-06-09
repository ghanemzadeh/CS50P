fruits = {
    "apple": 130,
    "avocado california": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "Lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "ptrawberries": 50,
    "Sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}

item = input("Item: ").lower

if item in fruits:
    print("Calories: ", fruits(item))
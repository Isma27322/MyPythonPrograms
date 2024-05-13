import random
import os
import time
import sys

# Constants
DIRECTIONS = ["north", "south", "east", "west"]
DIRECTIONS2 = ["n","s","e","w"]

ANIMALS = [
    "tiger", "elephant", "monkey", "snake",
    "crocodile", "parrot", "giraffe", "lion",
    "zebra", "panda", "koala", "hippo",
    "rhinoceros", "jaguar", "ostrich", "leopard",
    "kangaroo", "gorilla", "hyena", "chimpanzee",
    "gazelle", "armadillo", "seagull", "octopus",
    "buffalo", "capybara", "elephant seal", "flamingo",
    "mongoose", "otter", "platypus", "quokka",
    "red panda", "sloth", "tapir", "uakari",
    "vulture", "wallaby", "x-ray tetra", "yak",
    "zebu", "anteater", "baboon", "chameleon",
    "dingo", "elephant bird", "fennec fox", "gibbon",
    "hedgehog", "iguana", "jaguarundi", "koala",
    "lemur", "manatee", "numbat", "orangutan",
    "penguin", "quokka", "rhinoceros beetle", "serval",
    "tarsier", "umbrellabird", "vampire bat", "walrus",
    "xenopus", "yabby", "zebrafish", "anaconda"
]

FOOD_ITEMS = [
    "banana", "apple", "berries", "coconut",
    "mango", "pineapple", "watermelon", "orange",
    "grapes", "kiwi", "papaya", "pear",
    "peach", "avocado", "guava", "passion fruit",
    "dragon fruit", "fig", "lime", "plum",
    "apricot", "blackberry", "cherry", "durian",
    "elderberry", "feijoa", "grapefruit", "honeydew",
    "jackfruit", "kiwifruit", "lychee", "mulberry",
    "nectarine", "olive", "pomegranate", "quince",
    "raspberry", "strawberry", "tangerine", "ugli fruit",
    "vanilla bean", "watercress", "yam", "zucchini",
    "almond", "beetroot", "cabbage", "dates",
    "endive", "fennel", "garlic", "hazelnut",
    "iceberg lettuce", "jicama", "kale", "leek",
    "mushroom", "nopales", "okra", "parsnip"
]

TREASURES = [
    "gold", "diamonds", "jewels", "emerald",
    "sapphire", "ruby", "silver", "amethyst",
    "topaz", "pearl", "opal", "aquamarine",
    "citrine", "garnet", "tourmaline", "peridot",
    "moonstone", "agate", "jade", "onyx",
    "alexandrite", "beryl", "coral", "danburite",
    "enstatite", "fire opal", "goshenite", "heliodor",
    "iolite", "jadeite", "kunzite", "labradorite",
    "moldavite", "nephrite", "obsidian", "pyrite",
    "quartz", "rhodonite", "sugilite", "tanzanite",
    "uvarovite", "variscite", "wulfenite", "xenotime",
    "yellow diamond", "zircon", "ammonite fossil", "baltic amber",
    "celtic brooch", "diamond tiara", "egyptian scarab", "fossilized trilobite",
    "golden chalice", "holy grail", "inca mask", "jade dragon",
    "knight's helmet", "loch ness monster egg", "medieval sword", "norse rune stone"
]

OBJECTS = [
    "wall", "gate", "mysterious statue", "ancient ruins",
    "waterfall", "cave entrance", "abandoned camp", "riverside",
    "secret pathway", "enchanted tree", "volcano crater", "hidden cavern",
    "ancient temple", "sacred altar", "lost city", "forbidden forest",
    "mystic pond", "ruined bridge", "sunken ship", "enchanted garden",
    "crystal cave", "dragon's lair", "floating island", "ghostly mansion",
    "hidden treasure chest", "island of the lost", "jungle waterfall", "key to the unknown",
    "labyrinth of mirrors", "magical portal", "narrow mountain pass", "ocean abyss",
    "portal to another dimension", "quicksand pit", "riddle of the sphinx", "sacred waterfall",
    "time-worn pyramid", "underground catacombs", "valley of the ancients", "whispering windmill",
    "xylophone of the spirits", "yeti's cave", "zodiac observatory", "ancient book of spells"
]


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_intro():
    clear_screen()
    print("Welcome to the Jungle Adventure!")
    print("You find yourself in the heart of a dense jungle.")
    print("Your goal is to explore the jungle, find treasures, and survive encounters with wild animals.")
    print("Be careful, as your decisions will determine your fate!")

def choose_direction():
    print("Available directions:", ", ".join(DIRECTIONS))
    while True:
        direction = input("Which direction do you want to go? ").lower()
        if direction in DIRECTIONS or DIRECTIONS2:
            return direction
        else:
            print("Invalid direction. Please choose a valid direction.")

def encounter_animal():
    animal = random.choice(ANIMALS)
    print(f"Watch out! You encountered a wild {animal}!")
    if animal == "tiger":
        print("Run for your life!")
    elif animal == "elephant":
        print("Stay calm and avoid any sudden movements.")
    elif animal == "monkey":
        print("Keep your distance and avoid eye contact.")
    else:
        print("Carefully step back and give it space.")
    return animal

def find_food():
    food = random.choice(FOOD_ITEMS)
    print(f"You found some {food}. It will keep you energized on your journey.")
    return food

def find_treasure():
    treasure = random.choice(TREASURES)
    print(f"Congratulations! You discovered a hidden treasure of {treasure}.")
    return treasure

def handle_object_encounter(object_name):
    if object_name == "wall":
        print("You encounter a tall, impenetrable wall.")
        action = input("What would you like to do? (turn around/walk around/jump) ").lower()
        if action == "turn around":
            print("You turn around and find a different path.")
        elif action == "walk around":
            print("You try to walk around the wall, but it takes you some time.")
            print("Be cautious, as you might get lost.")
        elif action == "jump":
            print("You attempt to jump over the wall.")
            if random.random() < 0.7:
                print("Success! You managed to jump over the wall.")
            else:
                print("Oh no! Your jump didn't go as planned, and you fall back.")
        else:
            print("Invalid action. Please choose a valid action.")
    elif object_name == "gate":
        print("You encounter a closed gate.")
        action = input("What would you like to do? (turn around/walk around/try to open) ").lower()
        if action == "turn around":
            print("You decide to turn around and find an alternative route.")
        elif action == "walk around":
            print("You carefully walk around the gate and continue your journey.")
        elif action == "try to open":
            print("You attempt to open the gate.")
            if random.random() < 0.6:
                print("Success! The gate opens, and you pass through.")
            else:
                print("The gate seems stuck, and you are unable to open it.")
                print("You will need to find a key or another way around.")
        else:
            print("Invalid action. Please choose a valid action.")
    else:
        print("You encounter something intriguing but can't figure out what it is.")
        print("You decide to investigate further and keep it in mind during your adventure.")

def is_edge_of_jungle(x, y, size):
    return x == 0 or x == size - 1 or y == 0 or y == size - 1

def play_jungle_adventure():
    print_intro()
    size = random.randint(4,60)  # Size of the jungle grid
    x, y = size // 2, size // 2  # Starting position in the middle
    health = random.randint(-100,500)
    while health < 0:
        print("We apologize, but your health is either negitive or zero. We are trying to fix the problem.")
        time.sleep(random.randint(0,5))
        if random.randint(1, 0) == 0:
            print("We apologize for the inconvenience, but we were not able to fix the problem.")
            print("Game over, feel free to play again.")
            sys.exit()
        else:
            min_value = min(50, abs(health) * 2)
            max_value = max(50, abs(health) * 2)

            health = health + random.randint(min_value,max_value)
            time.sleep(random.randint(0,5))
            if (health > 0):
                print("We have fixed the problem. You can continue playing.")
    inventory = []
    while True:
        print("\n-----------------------------------")
        print(f"Health: {health}")
        direction = choose_direction()
        if random.random() < 0.2:
            health = health -  random.randint(10,50)
            if health <= 0:
                print("You got attacked and couldn't survive. Game over!")
                break
        else:
            print("You continue your journey through the jungle.")
            if random.random() < 0.1:
                food = find_food()
                health = health + random.randint(10,50)
                inventory.append(food)
            if random.random() < 0.05:
                treasure = find_treasure()
                inventory.append(treasure)
            if random.random() < 0.1:
                object_name = random.choice(OBJECTS)
                handle_object_encounter(object_name)

            # Move in the chosen direction
            if direction == "north" or "n":
                y -= random.randint(1,20)
            elif direction == "south" or "s":
                y += random.randint(1,20)
            elif direction == "east" or "e":
                x += random.randint(1,20)
            elif direction == "west" or "w":
                x -= random.randint(1,20)

            # Check if the player has reached the edge of the jungle and won the game
            if is_edge_of_jungle(x, y, size):
                print("Congratulations! You have successfully reached the edge of the jungle!")
                print("You won the game!")
                break

        print("Inventory:", ", ".join(inventory))
        decision = input("Do you want to continue exploring? (yes/no) ").lower()
        if decision.lower() not in ("yes", "ye", "y", "ys"):
            print("Thanks for playing Jungle Adventure. See you next time!")
            break

if __name__ == "__main__":
    play_jungle_adventure()
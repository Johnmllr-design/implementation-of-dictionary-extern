# this is a file for the second project in the externship

inventory = {}      # starting with an empty dictionary global variable

# implemment the functionality

def add(key, val):
    inventory[key] = val        # declare inventory[key] to be val

def update(key, val):
    inventory[key] = val        # update key to be val

def remove(key):
    inventory.pop(key)          # pop the key

def print_dict():
    for key in inventory.keys():
        print("key " + str(key) + " value " + str(inventory[key]))
    
def get_price():
    total = 0
    for key in inventory.keys():
        total += (inventory[key][0] * inventory[key][1])         # tally the different sums
    return total

    
# here's a demonstration of the functionality

inventory = {
"apple": (10, 2.5),
"banana": (20, 1.2)
}   # declare an example inventory

print_dict()        # print the dict

print("adding 15 mangoes with price 3")
add("mango", (15, 3))    # add in the mango

print("price is " + str(get_price()))              # print the total price

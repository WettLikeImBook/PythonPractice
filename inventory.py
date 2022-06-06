# Dictionary of players inventory
playerInventory = {'Arrows': 12,
                   'Gold Coins': 42,
                   'Rope': 1,
                   'Torch': 6,
                   'Dagger': 1}

# Function that will print players current inventory
def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(k + ':', v)
        item_total = item_total + v
    print('Total Items: ' + str(item_total))

displayInventory(playerInventory)
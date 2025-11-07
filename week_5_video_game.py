def find_item_index(item_names, item_name):
    for i in range(len(item_names)):
        if item_names[i] ==item_name:
            return i
    return -1

def process_inventory_events(initial_items, initial_quantities, events):
    items = initial_items[:]          
    quantities = initial_quantities[:] 

    for event in events:
        command = event[0]

        if command =="PICKUP":
            name = event[1]
            amount = event[2]
            idx = find_item_index(items, name)

            if idx != -1:
                quantities[idx] = quantities[idx] + amount
            else:
                items.append(name)
                quantities.append(amount)

        elif command=="USE":
            name = event[1]
            amount = event[2]
            idx = find_item_index(items, name)

            if idx != -1 and quantities[idx] >= amount:
                quantities[idx] = quantities[idx] - amount
                if quantities[idx] <= 0:
                    qty_value = quantities[idx]
                    items.remove(name)
                    quantities.remove(qty_value)

        elif command== "DROP":
            name = event[1]
            idx = find_item_index(items, name)

            if idx != -1:
                qty_value = quantities[idx]
                items.remove(name)
                quantities.remove(qty_value)

    return items, quantities

items = ["Sword", "Health Potion", "Gold Coin"]
quantities = [1, 5, 100]
game_events = [
    ["PICKUP", "Gold Coin", 50],
    ["USE", "Health Potion", 2],
    ["DROP", "Sword"],
    ["PICKUP", "Magic Scroll", 1],
    ["USE", "Health Potion", 3]
]

final_items, final_quantities = process_inventory_events(items, quantities, game_events)
print("Final Inventory:")
print("final_items:", final_items)
print("final_quantities:", final_quantities)

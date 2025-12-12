# You are building a checkout system.

# inventory: A dictionary mapping item names to prices. Warning: 
# Some items in the inventory have corrupted prices (set to None or negative numbers).
# cart: A list of item names a user wants to buy.
# Write a function checkout(inventory, cart) that:

# Iterates through the cart.
# Try:
# Look up the item in inventory.
# If the price is None, raise a TypeError (“Price missing”).
# If the price is less than 0, raise a ValueError (“Invalid price”).
# Add the price to the total_cost.
# Except:
# Handle KeyError (Item not in store): Print "Item not found: [name]".
# Handle TypeError / ValueError (Bad data in store): Print "Data error for [name]: [reason]".
# Count how many items failed to process.
# Return a tuple: (total_cost, failed_count).





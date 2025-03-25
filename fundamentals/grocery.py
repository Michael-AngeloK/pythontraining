# Create a program to manage a grocery list.

groceries = ["milk", "bread", "eggs"]
essentials = ("salt", "sugar")

while True:
  print("\nGrocery List Management")
  print("1. Add item")
  print("2. Remove item")
  print("3. View item")
  print("4. Check essentials")
  print("5. Exit")

  choice = input("Choose one: ")
  if choice == "1":
    new_item = input("Give an item to insert: ")
    if new_item not in groceries:
      groceries.append(new_item)
      print(f"{new_item} is added!")
    else:
      print(f"{new_item} is already listed.")
      
  elif choice == "2":
    remove_item = input("Give an item to be removed: ")
    if remove_item in groceries:
      groceries.remove(remove_item)
      print(f"{remove_item} is now removed!")
    else:
      print(f"This item in not in the list.")
    
  elif choice == "3":
    for item in groceries:
      print(f"- {item}")
    
  elif choice == "4":
    print("Essential items(unchangable): ", essentials)
    missing = [item for item in essentials if item not in groceries]
    if missing:
      print("You're missing:", ", ".join(missing))
    else:
      print("You're not missing anything!")
    
  elif choice == "5":
    print("\nExiting...")
    break
  
  
  


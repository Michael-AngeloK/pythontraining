gradebook = {"Alice": 85, "Bob": 9}

while True:
  print("\nGradebook Manager: ")
  print("1. Add")
  print("2. Update")
  print("3. Calculate average")
  print("4. Print top-scoring student")
  print("5. View all students")
  print("6. Exit")
  
  choice = input("Choose an option: ")
  if choice == "1" or choice == "Add":
    student = input("Name the student you want to add: ")
    if student not in gradebook:
      grade = input("Give him/her a grade: ")
      gradebook[student] = grade
    else:
      print(f"{student} is already listed in the gradebook")
          
  if choice == "2":
    print("2")
    
  if choice == "3":
    print("3")
    
  if choice == "4":
    print("4")
    
  if choice == "5":
    for n in gradebook:
      print(f"- {n}: {gradebook.get(n)}")
      
    
  if choice == "6":
    print("Exiting...")
    break
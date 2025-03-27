gradebook = {"Alice": 85, "Bob": 9}
MINIMUM_GRADE = 0
MAXIMUM_GRADE = 100

while True:
  print("\nGradebook Manager: ")
  print("1. Add")
  print("2. Update")
  print("3. Calculate average")
  print("4. Print top-scoring student")
  print("5. View all students")
  print("6. Exit")
  
  choice = input("Choose an option: ")
  if choice == "1" or choice == "add":
    student = input("Name the student you want to add: ")
    if student not in gradebook:
      while True:
        grade = input("\nGive this student a grade: ")
        if int(grade) > MINIMUM_GRADE and int(grade) <= MAXIMUM_GRADE: 
          gradebook[student] = int(grade)
          break
        else:
          print("Grade is invalid")
    else:
      print(f"{student} is already listed in the gradebook.")
          
  if choice == "2" or choice == "update":
    student = input("Choose a student to update their grade: ")
    if student in gradebook:
      grade = input("\nGive this student a grade: ")
      if int(grade) > MINIMUM_GRADE and int(grade) <= MAXIMUM_GRADE: 
        gradebook[student] = int(grade)
      else:
        print("Grade is invalid.")
    else:
      print("This student is not listed here.")
    
  if choice == "3" or choice == "calculate":
    sum = 0
    for student in gradebook:
      sum += gradebook[student]
    print(f"{float(sum / len(gradebook))} is the average grade")
    
  if choice == "4" or choice == "print":
    highest_student = next(iter(gradebook))
    for student in gradebook:
      if gradebook[student] > gradebook[highest_student]:
        highest_student = student
    print(f"The highest student is {highest_student}.")
    
  if choice == "5" or choice == "view":
    for n in gradebook:
      print(f"- {n}: {gradebook.get(n)}")
      
    
  if choice == "6" or choice == "exit":
    print("Exiting...")
    break
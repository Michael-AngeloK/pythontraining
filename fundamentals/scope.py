import math

def calculate_area(length, width=0, shape="square"):
  if (shape == "square"):
    return length ** 2
  elif (shape == "rectangle"):
    return length * width
  elif (shape == "circle"):
    return 2 * 3.14 * length
  else:
    return "invalid shape"

def calculate_perimeter(length, width=0, shape="square"):
  if (shape == "square"):
    return length * 4
  elif (shape == "rectangle"):
    return 2 * (length + width)
  elif (shape == "circle"):
    return 2 * math.pi * length
  else:
    return "invalid shape"

shape = input("Enter shape you want to calculate: ").lower()
length = float(input("Enter length of shape here: "))

if shape in ["rectangle"]:
  width = input("Enter width of shape here: " or length)
else:
  width = None
  
area = calculate_area(length, width, shape)
perimeter = calculate_perimeter(length, width, shape)

print("Area is of shape is:", area)
print("Perimeter is of shape is:", perimeter)
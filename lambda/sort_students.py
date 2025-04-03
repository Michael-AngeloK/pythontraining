gradebook = [("Alice", 88), ("Bob", 92), ("Charlie", 75)]

sorted_gradebook = sorted(gradebook, key=lambda a: a[1], reverse=True)

print(sorted_gradebook)
# X = ["omit ", " Tahamid "]
# X.append(" Ahanaf ")  # Adds an element at the end of the list
# # X.clear() 	# Removes all the elements from the list
# # Y= X.copy()  # Removes all the elements from the list
# X.count("omit")	 # Returns the number of elements with the specified value
# print(X)

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
counts = {}

for i in points:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1

# Print the counts
for key, value in counts.items():
    if value==2:
     print(key)


# ------------------------------------------
#  PART 1: EASY LEVEL (Understanding Basics)
# ------------------------------------------

# Question 1: Create a list named fruits that stores three fruit names. A list is used to store multiple values in one variable.
fruits: list  = ["Apple", "Banana", "Cherry"]
print(fruits)

# Question 2: Print the second item from the fruits list. Remember that lists start counting from index 0.
print("Staring from Beginning 2nd Item: ",fruits[1])
print("Staring from Reverse 2nd Item: ",fruits[-2])

# Question 3: Change the last item in the fruits list to a new fruit name and print the updated list.
# This checks if you know how to modify list values.
fruits[-1] = "Mango"
print("After Modifying Last Item from List: ",fruits)

# Question 4: Create a tuple named numbers that stores four numbers. A tuple is like a list but its values cannot be changed.
numbers: tuple = (10, 20, 30,40 )
print("Tuple of Numbers:",numbers)

# Question 5: Print how many items are inside the numbers tuple.
print(f"There are {len(numbers)} items inside the numbers tuple")


# --------------------------------------------------
#  PART 2: MEDIUM LEVEL (Using Methods & Structures)
# ---------------------------------------------------

# Question 6: Add a new fruit to the fruits list using a list method, then print the list.
# This tests how to add values to an existing list.
fruits.append("Watermelon")
print("After Adding New fruit in list",fruits)


# Question 7: Remove one fruit from the fruits list using a list method, then print the list.
# This checks how to delete items from a list.
fruits.remove("Mango")
print("After Removing a fruit in list",fruits)


# Question 8: Convert the numbers tuple into a list, store it in a new variable, and print it.
# This checks if you understand type conversion.
numbers_tuple_list_convert: list = list(numbers)
print("Converting Tuple into List Data Type",numbers_tuple_list_convert)


# Question 9: Create a dictionary named student with keys name, age, and course. A
# dictionary stores data using labels called keys.
student: dict = {
    "name": "Muneer",
    "age": 30,
    "course": "Agentic AI"
}
print(student)


# Question 10: Print the value of the course key from the student dictionary.
print(student.get("course", "DefaultCourseValueIfKeyNotExist"))


# --------------------------------------------------
#  PART 3: HARD LEVEL (Thinking in Code)
# ---------------------------------------------------

# Question 11: Use a for loop to print each fruit from the fruits list one by one.
# This checks your understanding of loops with lists.
for fruit in fruits:
    print(fruit)
else:
    print("End printing list loop ")


# Question 12: Check if a number exists inside the numbers list and print True or False.
# This tests how Python checks values inside a list.
if 20 in numbers_tuple_list_convert:
    print("20 exists in list")
else:
    print("20 does not exists in list")


# Question 13: Add a new key called grade to the student dictionary and give it a value.
# This checks how to update dictionaries.
student["grade"] = "A+"
print("After Adding grade key in student dictionary:",student)


# Question 14: Remove any one key from the student dictionary using a dictionary method, then print the dictionary.
del student["age"]
print("After deleting Age key in student dictionary:",student)


# Question 15: Combine two lists together and print the final list. This checks how lists can be joined in Python.
fruits_list2: list = ["Orange","Grapes","Strawberry"]
fruits.extend(fruits_list2)
print("Combining 2 List",fruits)

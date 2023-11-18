"""
Create a class named 'Student' with the variable 'name' and 'roll_no'. And write a Display method to display the name
 and roll_no.Assign the value of roll_no as '2' and that of name as "John" by creating an object of the class Student.
"""
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")

student_object = Student("John", 2)
student_object.display()


# Don't use __init__ method
# class Student:
#     def X (self, name, roll_no):
#         self.name = name
#         self.roll_no = roll_no
# object = Student()
# object.X("omit",810)
#
# print(f" name = {object.name}  and roll ({object.roll_no}) ")

class Parent:
    def speak(self):
        print("Parent class speaks.")

class Child(Parent):
    def talk(self):
        print("Child class talks.")

# Creating an instance of the Child class
child_instance = Child()

# Calling methods from both the Parent and Child classes
child_instance.speak()
child_instance.talk()

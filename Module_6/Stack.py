# # class Stack:
# #     def __init__(self):
# #         self.items = []
# #
# #     def is_empty(self):
# #         return len(self.items) == 0
# #
# #     def push(self, item):
# #         self.items.append(item)
# #
# #     def pop(self):
# #         if not self.is_empty():
# #             return self.items.pop()
# #         else:
# #             return "Stack is empty"
# #
# #     def peek(self):
# #         if not self.is_empty():
# #             return self.items[-1]
# #         else:
# #             return "Stack is empty"
# #
# #     def size(self):
# #         return len(self.items)
# # # Create a stack
# # stack = Stack()
# #
# # # Push elements onto the stack
# # stack.push(5)
# # stack.push('hello')
# # stack.push('Omit')
# #
# # # Get the size of the stack
# # print("Size of stack:", stack.size())
# #
# # # Peek at the top element of the stack
# # print("Top element:", stack.peek())
# #
# # # Pop elements from the stack
# # print(stack.pop())
# # print(stack.pop())
# # print(stack.pop())
# # print(stack.pop())  # Trying to pop from an empty stack
#
#
#
#

def create_stack():
    return []

def is_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        return "Stack is empty"
# Create an empty stack
stack = create_stack()

# Push elements onto the stack
push(stack, 5)
push(stack, 'hello')
push(stack, True)

# Pop elements from the stack
print(pop(stack))
print(pop(stack))
print(pop(stack))
print(pop(stack))  # Trying to pop from an empty stack








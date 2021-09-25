stack = ['book1','book2','book3']
if len(stack) == 0:
    print("Stack is empty")

else:
    stack.append('book4')
    print(stack)
    stack.pop()
    print(stack)
    stack.append('book5')
    print(stack)

#'book1','book2','book3','book5'
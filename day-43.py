"""
This problem was asked by Amazon.

Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.

"""
STACK = []

def push(val):
    STACK.append(val)
    print(STACK)
    
def pop():
    return STACK.pop()

def max_num():
    return max(STACK)

if __name__ == "__main__":
    ch = 1
    while(ch!=0):
        ch = int(input("Enter the choise \n 1. push \t 2. pop \t 3. max\n"))

        if ch == 1:
            val = int(input("Enter value for push\n"))
            push(val)

        elif ch == 2:
            print(pop())

        elif ch == 3:
            print(max_num())

        else:
            break

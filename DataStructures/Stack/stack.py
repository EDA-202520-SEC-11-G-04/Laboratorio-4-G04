# DataStructures/Stack/stack.py

def new_stack():
   
    return {"elements": []}


def push(stack, element):

    stack["elements"].append(element)


def pop(stack):
 
    if is_empty(stack):
        return None
    return stack["elements"].pop()


def top(stack):
   
    if is_empty(stack):
        return None
    return stack["elements"][-1]


def is_empty(stack):

    return len(stack["elements"]) == 0


def size(stack):

    return len(stack["elements"])

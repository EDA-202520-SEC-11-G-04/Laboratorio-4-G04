# DataStructures/Queue/queue.py

def new_queue():

    return {"size"}, {"elements", []}

def size(my_queue):
    
    return len(my_queue)

def is_empty(my_queue):
    if my_queue.size == 0:
        return True
    else:
        return False
    
def enqueue(my_queue, element):
    new_element = {"info": element, "next": None}

    if my_queue.size == 0:
        my_queue["first"] = new_element
        my_queue["last"] = new_element
    else:  
        my_queue["last"]["next"] = new_element
    my_queue["size"] += 1
    return my_queue

def dequeue(my_queue):
    if my_queue.is_empty():
            print("La cola está vacía.")
            return None
    
    deleted_node = my_queue.first    
    my_queue.first = my_queue.first.next
    my_queue.size -= 1
        
    if my_queue.first is None:
        my_queue.last = None
         
    return deleted_node.value

def peek(my_queue):
    return my_queue.first


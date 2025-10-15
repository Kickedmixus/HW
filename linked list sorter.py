class Node:
    def __init__(self, data, nnext=None):
        self.data = data
        self.nnext = nnext
    def get(self):
        return self.value
        
        
#WHY NODE??? OR LINKED LIST HELP
head = None

head = None
def insert(value): #insert(54)
  NewNode = Node(value)
  if head == None:
    head = NewNode
    return
  current = head
  while current.next:
    current = current.next
  current.next = NewNode # Tail NewNode

def get_middle(head):
        if not head:
            return head
        slow = head
        fast = head.nnext
        while fast and fast.nnext:
            slow = slow.nnext
            fast = fast.nnext.nnext
        return slow

def merge_sort(head):
        #Base case: 0 or 1 node
        if not head or not head.nnext:
            return head

        #Split the list in half
        middle = get_middle(head)
        next_to_middle = middle.nnext
        middle.nnext = None  # Split it

        #Recursively sort both halves
        left = merge_sort(head)
        right = merge_sort(next_to_middle)

        #Merge the sorted halves
        sorted_list = sorted_merge(left, right)
        return sorted_list

def sorted_merge(a, b):
        if not a:
            return b
        if not b:
            return a

        if a.data <= b.data:
            result = a
            result.nnext = sorted_merge(a.nnext, b)
        else:
            result = b
            result.nnext = sorted_merge(a, b.nnext)
        return result

def sort(head):
  if not head or not head.nnext:
    return head

  middle = get_middle(head)
  next_to_middle = middle.nnext
  middle.nnext = None

  left = merge_sort(head)
  right = merge_sort(next_to_middle)

  sorted_list = sorted_merge(left, right)
  return sorted_list

#Breath-First Search WITH WHILE LOOP
def BFS(graph, start):
    visited = []

    #but i made it work???
    queue = [start]  # FIFO

    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.append(current)
            print current
            for neighbor in graph.get(current, []):#HUH???(AttributeError: 'Node' object has no attribute 'get' on line 35 in main.py)
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    return visited

# Example graph as dictionary
graph = {
    8: [3, 10],
    3: [1, 6],
    10: [14],
    1: [],
    6: [4, 7],
    14: []
}



print sort(Node(5,Node(12,Node(2,Node(6,Node(34,Node(21,Node(8,Node(54,Node(27,Node(11))))))))))).data

#i am perplexed

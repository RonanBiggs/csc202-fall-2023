from dataclasses import dataclass

   

class Node:
    item = None
    index = None
    left_child = None
    right_child = None

    def __init__(self, item):
        self.item = item

class MaxHeap:
    list = [None]*256
    root = None




    '''inserts "item" into the heap, returns true if successful, false
if there is no room in the heap
"item" can be any primitive or ***object*** that can be
compared with other
items using the < operator'''
    def enqueue(self, item):
        new_node = Node(item)
        if self.list[255] is not None: #heap is full
            return False
        if self.root is None: #heap is empty
            self.root = new_node
            self.list[0] = new_node
            new_node.index = 0
            return True
        for i in range(len(self.list)):
            if self.list[i] is None:
                self.list[i] = new_node
                new_node.index = i

                #if its even meaning right node
                if i % 2 == 0:
                    self.list[int(i-1/2)].right_child = new_node
                    #if its odd meaning left node
                else:
                    self.list[int(i - 1 / 2)].left_child = new_node
                break


        self._enqueue_reorder(self, new_node)

        #find where to put node
    def _enqueue_reorder(self, new_node):
        while new_node.item > self.list[int(new_node.index - 1 / 2)].item:
            self.swap(self, new_node, self.list[int(new_node.index - 1 / 2)])


    def swap(self, node1, node2):
        self.list[node1.index], self.list[node2.index] = self.list[node2.index], self.list[node1.index]
        node1.index, node2.index = node2.index, node1.index
        if self.list[node1.index*2] is not None:
            node1.left_child = self.list[node1.index*2]
        if self.list[node1.index*2+1] is not None:
            node1.right_child = self.list[node1.index*2+1]
        if self.list[node2.index*2] is not None:
            node1.left_child = self.list[node2.index*2]
        if self.list[node2.index*2+1] is not None:
            node1.right_child = self.list[node2.index*2+1]

MH = MaxHeap
MH.enqueue(MH, 5)
MH.enqueue(MH, 62)
MH.enqueue(MH, 61)
MH.enqueue(MH, 2)
MH.enqueue(MH, 12)
for i in MH.list:
    if i is not None:
        print(i.item)
    else:
        print(i)



    """returns max without changing the heap, returns None if the heap is empty"""

    def peek(self):
        if self.root is None:
            return None
        else:
            return self.root.value

    """returns max and removes it from the heap and restores the heap
    property returns None if the heap is empty"""

    def dequeue(self):
        pass

    """returns a list of contents of the heap in the order it is
    stored internal to the heap.
    (This may be useful for in testing your implementation.)"""

    def contents(self):
        list = []
        self.in_order_recursive(self.root)
        return list

    def in_order_recursive(self, current_node):
        if current_node is not None:
            self._in_order_recursive(current_node.left_child)
            list.append(current_node.value)
            self._in_order_recursive(current_node.right_child)

    """Discards all items in the current heap and builds a heap from
    the items in alist using the bottom-up construction method.
    If the capacity of the current heap is less than the number of
    items in alist, the capacity of the heap will be increased to
    accommodate the items in alist"""

    def build_heap(self, alist):
        pass

    """returns True if the heap is empty, false otherwise"""

    def is_empty(self):
        return self.get_size() == 0

    """returns True if the heap is full, false otherwise"""

    def is_full(self):
        return self.get_size() == self.get_capacity()

    """this is the maximum number of a entries the heap can hold
    1 less than the number of entries that the array allocated to hold"""

    def get_capacity(self):
        pass

    """the actual number of elements in the heap, not the capacity"""

    def get_size(self):
        pass

    """where the parameter i is an index in the heap and perc_down
    moves the element stored
    at that location to its proper place in the heap rearranging
    elements as it goes."""

    def perc_down(self, i):
        pass

    """where the parameter i is an index in the heap and perc_up moves
    the element stored
    at that location to its proper place in the heap rearranging
    elements as it goes."""

    def perc_up(self, i):
        pass

    """perform heap sort on input alist in ascending order
    This method will discard the current contents of the heap, build a
    new heap using
    the items in alist, then mutate alist to put the items in
    ascending order"""

    def heap_sort_ascending(self, alist):
        pass

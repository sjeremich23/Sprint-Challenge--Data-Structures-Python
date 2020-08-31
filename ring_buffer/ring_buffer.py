from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if the length is less than capacity
        if self.storage.length < self.capacity:
            # add item to the end
            self.storage.add_to_tail(item)
            # make the current item the tail
            self.current = self.storage.tail

        # if RingBuffer's length is at capacity
        elif self.storage.length == self.capacity:
            # if there is no current NEXT head, then the head is the oldest
            if not self.current.next:
                # remove oldest item
                self.storage.remove_from_head()
                # add in the item
                self.storage.add_to_head(item)
                # set currently placed item to the head, because you are ALWAYS removing and replacing the oldest item
                self.current = self.storage.head
            # if there is a next
            else:
                # delete the next item
                self.current.next.delete()
                # replace the next with the new item
                self.current.insert_after(item)
                # set the item to current
                self.current = self.current.next

    def get(self):
        list_contents = []

        item = self.storage.head
        # while there is an item
        while item:
            # appending the item value to the array list_contents
            list_contents.append(item.value)
            # assigning item now to item.next, then it happens again
            # as long as there is an item it will keep going
            # once it goes through all items ->
            item = item.next
        # -> it will then return the list
        return list_contents

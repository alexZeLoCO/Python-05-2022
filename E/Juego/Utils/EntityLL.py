from Entity.Entity import Entity
from random import random

class EntityLL:
    def __init__ (self):
        """
        EntityLL (void)
        Creates a new Linked List
        """
        self.head = Node (None, None, None)
        self.tail = Node (None, None, None)
        self.size = 0

    def size (self):
        """
        size (void)
        Returns the size of this Linked List
        """
        return self.size

    def add (self, entity):
        """
        add (entity:Entity)
        Adds the entity to the Linked List
        """
        if (self.size == 0):
            self.head.data = entity
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            self.tail = Node (self.tail.prev, entity, Node (None, None, None))
            self.tail.next.prev = self.tail
            self.tail.prev.next = self.tail
            self.tail = self.tail.next
        self.size+=1

    def remove (self, entity):
        """
        remove (entity:Entity)
        Removes the entity from the Linked List
        Returns True if the entity was removed.
        Retrus False if the entity was not on the Linked List.
        """
        if (self.head.data == entity):
            self.removeHead()
            return True
        elif (self.tail.prev.data == entity):
            self.removeTail()
            return True
        else:
            node = self.head
            for i in range (0, self.size, 1):
                if (node.data == entity):
                    node.previous = node.next
                    node.next = node.previous
                    self.size-=1
                    return True
        return False

    def removeHead (self):
        """
        removeHead (void)
        Returns and removes the first element from the Linked List
        """
        out = self.head.data
        self.head = self.head.next
        self.head.previous = None
        self.size-=1
        return out

    def removeTail (self):
        """
        removeTail (void)
        Returns and removes the last element from the Linked List
        """
        out = self.tail.prev.data
        self.tail = self.tail.prev
        self.tail.next = None
        self.tail.data = None
        self.size-=1
        return out

    def switch (self, current, new):
        """
        switch (current:Entity, new:Entity)
        Switches the current entity from the new one.
        Returns the old entity.
        """
        node = self.getNode(current)
        out = node.data
        node.data = new
        return out

    def get (self, idx:int):
        """
        get (idx:int)
        Returns the element in position idx of the Linked List
        Returns False if the element was not found
        """
        node = self.head
        for i in range (int(idx)):
            node = node.next
        return node.data

    def getNode (self, data:Entity):
        """
        get (data:Entity)
        Returns the node that has the data
        Returns False if the node was not found
        """
        node = self.head
        for i in range (self.size):
            if (node.data == data):
                return node
            node = node.next
        return False

    def getRandom (self):
        """
        getRandom (void)
        Returns a random entity from the Linked List
        """
        return self.get(random()%(self.size))

    def toString (self):
        """
        toString (void)
        Returns a text-based representation of this Linked List
        """
        out = ""
        node = self.head
        for i in range (0, self.size, 1):
            out+="[" + node.data.toString() + "], "
            node = node.next
        return "{" + out[:len(out)-2] + "}"


class Node:
    def __init__ (self):
        """
        Node (void)
        Creates a new node
        """
        self.prev = None
        self.data = None
        self.next = None

    def __init__ (self, prev, entity, _next):
        """
        Node (prev:Node, entity:Entity, _next:Node)
        Creates a new node with a previous and next nodes and entity data
        """
        self.prev = prev
        self.data = entity
        self.next = _next

    def hasPrevious (self):
        """
        hasPrevious (void)
        Returns True if this node has a previous node
        """
        return self.prev != None

    def hasNext (self):
        """
        hasNext (void)
        Returns True if this node has a next node
        """
        return self.next != None

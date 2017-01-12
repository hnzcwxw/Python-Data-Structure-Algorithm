class Set:
    # Create an empty set instance
    def __init__(self):
        self._theElements = list()

    # Return the number of the items in the set
    def __len__(self):
        return len(self._theElements)

    # Determines if an element is in the set
    def __contains__(self, item):
        return item in self._theElements

    # Adds a new unique element to the set
    def add(self, element):
        if element not in self:
            self._theElements.append(element)

    # Remove an element from the set
    def remove(self, element):
        assert element in self, "The element must be in the set"
        self._theElements.remove(element)

    # Determines if two sets are equal
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        else:
            return self.isSubsetOf(other)

    # Determines if the set is a subset of setB
    def isSubsetOf(self, setB):
        for element in self:
            if element not in setB:
                return False
        return True

    # Creates a new set from union of this set and setB
    def union(self, setB):
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for element in setB:
            if element not in self:
                newSet._theElements.append(element)
        return newSet

    # Create a new set from the intersection : self set and setB
    def intersect(self, setB):
        newSet = Set()
        for element in self:
            if element in setB:
                newSet._theElements.append(element)
        return newSet

    # Create a new set from the difference : self set and setB
    def difference(self, setB):
        newSet = Set()
        for element in self:
            if element not in self.intersect(setB):
                self._theElements.append(element)

        for element in setB:
            if element not in self.intersect(setB):
                self._theElements.append(element)

    # Determines the set is empty or nat
    def isEmpty(self):
        if self.__len__() == 0:
            return True
        else:
            return False

    # Return an iterator for traversing the list of items
    def __iter__(self):
#        return self._theElements.__iter__()
        return _SetIterator(self._theElements)

class _SetIterator:
    def __init__(self, theSet):
        self._setRef = theSet
        self._curNdx = 0

    def __iter__(self):
        return self

    def next(self):
        if self._curNdx < len(self._setRef):
            entry = self._setRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            return StopIteration

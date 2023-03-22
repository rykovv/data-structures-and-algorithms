##
# @file bag.py
# 
# @brief Implementation of LinkedList Bag data structure and its test
#
# @section description_linkedlist_bag Description
# Implementation of LinkedList Bag data structure and its test
# 
# @section notes_linkedlist_bag Notes
# - 
# 
# @section todo_linkedlist_bag TODO
# -
#
# @section author_linkedlist_bag Author
# - Vladislav Rykov
#
##

class BagItem():
    """! BagItem Class """
    
    def __init__(self, item, count = 1):
        self.item = item
        self.count = count
        self.nextBagItem = None

    def __repr__(self):
        return f'{self.item} {self.count}'

class _LinkedListBagIterator():
        """! Iterator for LinkedListBag Class """
        def __init__(self, bag):
            self._bagItems = bag
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self._bagItems is None:
                raise StopIteration
            else:
                item = self._bagItems
                self._bagItems = self._bagItems.nextBagItem    
                return item

class LinkedListBag():
    """! LinkedList Bag Class """

    def __init__(self):
        self.items = None
        self.numItems = 0
        self.numItemsTotal = 0

    def add(self, item, count = 1):
        added = False
        itms = self.items

        while (not added):
            if itms is None:
                newBagItem = BagItem(item, count)
                newBagItem.nextBagItem = self.items
                self.items = newBagItem

                self.numItems += 1
                self.numItemsTotal += count
                added = True
            else:
                if itms.item is item:
                    itms.count += count

                    self.numItemsTotal += count
                    added = True
                else:
                    itms = itms.nextBagItem

    def remove(self, item, count = 1):
        done = False
        prev_item = None
        curr_item = self.items

        while (curr_item is not None and not done):
            if curr_item.item is item:
                curr_item.count -= count

                if curr_item.count <= 0:
                    if prev_item is not None:
                        prev_item.nextBagItem = curr_item.nextBagItem
                    else:
                        self.items = curr_item.nextBagItem
                    
                    self.numItems -= 1
                    self.numItemsTotal -= (curr_item.count + count)
                else:
                    self.numItemsTotal -= count

                done = True
            else:
                prev_item = curr_item
                curr_item = curr_item.nextBagItem

    def contains(self, item):
        itms = self.items
        ret = False

        while (itms is not None and not ret):
            if itms.item is item:
                ret = True
            else:
                itms = itms.nextBagItem

        return ret

    def __iter__(self):
        return _LinkedListBagIterator(self.items)

    def length(self):
        return self.numItems
    
    def lengthTotal(self):
        return self.lengthTotal

    def __repr__(self):
        itms = self.items
        ret = []

        while (itms is not None):
            ret.append(f'{itms.item} {itms.count}')
            itms = itms.nextBagItem

        return ' - '.join(ret) + f'\nTotal {self.numItems}/{self.numItemsTotal}'


lb = LinkedListBag()
print(lb)

# add
lb.add('pollo')
print(lb)

lb.add('repollo', 2)
print(lb)

lb.add('avena', 3)
print(lb)

lb.add('nueces', 2)
print(lb)

# iterator
for item in lb:
    print(item)

# remove
lb.remove('papas', 10)
print(lb)

lb.remove('pollo')
print(lb)

lb.remove('avena', 10)
print(lb)

# contains
print(lb.contains('nueces'))
print(lb.contains('avena'))

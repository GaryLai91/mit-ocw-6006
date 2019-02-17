# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 03:24:43 2019

@author: Gary
"""

class Heap():
    def __init__(self):
        self.array = []
        self.size = 0

    def __len__(self):
        return len(self.array)

    def heap_decrease_key(self, array, idx, key):
        if key > array[idx - 1]:
            raise ValueError("New key is bigger than current key")
        array[idx - 1] = key
        while (idx > 1) and (array[idx//2 - 1] > array[idx - 1]):
            temp = array[idx - 1]
            array[idx - 1] = array[idx//2 - 1]
            array[idx//2 - 1] = temp
            idx = idx // 2

    def append(self, key):
        self.size += 1
        self.array.append(key)  # Has to be something
        self.heap_decrease_key(self.array, self.size, key)

    def min(self):
        if len(self.array) == 0:
            return None
        return self.array[0]

    def pop(self):
        if len(self.array) < 1:
            return None
        max_ = self.array[0]
        self.array[0] = self.array[self.size - 1]
        del self.array[self.size - 1]
        self.size -= 1
        self.min_heapify(self.array, 1)
        return max_

    def min_heapify(self, array, index):
        smallest = index
        l = 2 * index
        r = l + 1

        if l - 1 < self.size:
            if array[l - 1] < array[index - 1]:
                smallest = l
            else:
                smallest = index

        if r - 1 < self.size:
            if array[r - 1] < array[smallest - 1]:
                smallest = r

        if smallest != index :
            temp = array[index - 1]
            array[index - 1] = array[smallest - 1]
            array[smallest - 1] = temp
            self.min_heapify(array, smallest)

    def build_min_heap(self):
        length = self.size // 2
        for i in range(length, 0, -1):
            self.min_heapify(self.array, i)



if __name__ == '__main__':
    heap = Heap()
    heap.append(16)
    heap.append(10)
    heap.append(4)
    print(heap.array)

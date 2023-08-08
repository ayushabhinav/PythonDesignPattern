from abc import ABC, abstractmethod
import random

class Sorting(ABC):
    
    @abstractmethod
    def sort(self):
        raise NotImplementedError
    

class BubbleSort(Sorting):
    def __init__(self, data):
        self.data = data
    
    def sort(self):
        for i in range(len(self.data)-1, 0, -1):
            self._do_sorting(i)
    
    def _do_sorting(self, pos):
        i = 0
        while i< pos:
            if self.data[i] > self.data[i+1]:
                self.data[i], self.data[i+1] = self.data[i+1], self.data[i]
            i += 1
        

class InsertionSort(Sorting):
    def __init__(self, data):
        self.data = data
        
    def sort(self):
        for i in range(len(self.data)):
            self._insert_into_place(i)
    
    def _insert_into_place(self, pos):
        item = self.data[pos]
        i = pos - 1
        while i >=0 and self.data[i] > item:
            self.data[i+1] = self.data[i]
            i = i - 1
        self.data[i+1] = item
        
        

class UserCode:
    def __init__(self):
        self.data = [random.randint(0,50) for _ in range(10)]
        print(self.data)
        self.sort = None
        
        
    def choose_stragety(self):
        print('''
              Choose the sort algorithms:
              1. Bubble Sort
              2. Insertion Sort
              
              please enter the number:
              ''')
        ans = int(input())
        
        if ans == 1:
            self.sort = BubbleSort(self.data)
        if ans == 2:
            self.sort = InsertionSort(self.data)
        
    def do_sorting(self):
        self.sort.sort()
        print(f'sorting Done by {self.sort.__class__.__name__}')
        print(self.data)    
        

if __name__ == "__main__":
    uc = UserCode()
    uc.choose_stragety()
    uc.do_sorting()



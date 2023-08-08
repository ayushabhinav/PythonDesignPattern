from abc import ABC
from typing import Any


# Observer Abstract Base class
class Observer(ABC):
    def __call__(self, *args, **kwargs):
        raise NotImplementedError
    
    def __str__(self) -> str:
        raise NotImplementedError

# Core Class
class Inventory:
    def __init__(self) -> None:
        self.observers = []
        self._product = None
        self._quantity = 0 
        
    def attach_obsever(self, observer:Observer):
        self.observers.append(observer)
        print(f'Observer {observer} added ')
        
    @property
    def product(self):
        return self._product
    
    @product.setter
    def product(self, value):
        self._product= value
        self._update_observer()
        
        
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        self._quantity += value
        self._update_observer()
        
    def _update_observer(self):
        for observer in self.observers:
            observer()
            
            
# Observer Concrete Class
class ConsoleObserver(Observer):
    def __init__(self, inventory) -> None:
        self.inventory = inventory
        
    def __call__(self, *args, **kwargs):
        print(f'Product:{self.inventory.product}')
        print(f'Quantity:{self.inventory.quantity}')
        
    def __str__(self) -> str:
        return self.__class__.__name__ 
        
# Observer Concrete Class
class FileObserver(Observer):
    def __init__(self, inventory) -> None:
        self.inventory = inventory        

    def __call__(self, *args, **kwargs):
        print(f'print to file: product :{self.inventory.product}')
        print(f'print to file: quantity :{self.inventory.quantity}')
                
    def __str__(self) -> str:
        return self.__class__.__name__
    

# Main Method
if __name__ == "__main__":
    i = Inventory()
    
    c = ConsoleObserver(i)
    f = FileObserver(i)
    
    i.attach_obsever(c)
    i.attach_obsever(f)
    
    
    print('------------START---------')
    i.product = 'Book'
    print('*' * 20)
    i.quantity = 10
    print('*' * 20)
    print('------------END---------')
    
    
    
    
    
    
    
    
    
    
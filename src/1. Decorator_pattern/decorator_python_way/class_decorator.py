import time
from typing import Any

class ExecutionTime():
    def __init__(self):
        pass
    
    def __call__(self, func) -> Any:
        def wrapper(*args, **kwargs):
            start_time = time.time()
            res = func(*args, **kwargs)
            end_time = time.time()
            print(f'time spent in execution:{end_time - start_time}')
            return res
        return wrapper
    
et = ExecutionTime()


@et
def do_sorting():
    import random
    num_list = [random.randint(0,100) for i in range(200)]
    num_list.sort()
    return num_list


res = do_sorting()
print(res)


###################################################################################################################


class FrequencyCounter():
    def __init__(self):
        self.counter = 0
        
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            self.counter += 1
            return func(*args, **kwargs)
        return wrapper


fc = FrequencyCounter()

@fc
def hello(name):
    pass

import random
for i in range(random.randint(10,20)):
    hello(i)


print(f'funcation called {fc.counter} times')






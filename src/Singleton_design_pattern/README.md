This design pattern alows only one instance of the object to exist.
The object is a sort of manager class. 

It is of two types:- 
    1. Module-level singleton -> objects created in module is singleton
    2. Classic Singleton ->  Only one object is created and shared wheneven new object creation reqest is received.
    3. Borg Singleton -> Multiple objects are created but they all share the same state. Change in state by one object is reflected in the state of all object.

    
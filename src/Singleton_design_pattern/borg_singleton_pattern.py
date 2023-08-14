class BorgSingleton:
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        """function to share the state between all the object of the class
        Returns:
            BrogSingleton Object: object of class BorgSingleton
        """
        obj = super().__new__(cls, *args, **kwargs)
        print("object created")
        obj.__dict__ = cls._shared_state
        return obj


# All objects refer to the same shared variable.
# Any modification by one object will have impact on all objects
# There are multiple objects as they have different address in print statement

bs1 = BorgSingleton()
bs1.name = "BS1"
print(f"BS1:{bs1}")
print(f"bs1 name:{bs1.name}")


bs2 = BorgSingleton()
print(f"BS2:{bs2}")
print(f"bs2 name:{bs2.name}")
bs2.type = "my_type"
print(f"BS2 type:{bs2.type}")

# Changes done by bs2 is reflected in bs1 object
print(f"bs1 variables: {bs1.__dict__}")

class Singleton:
    _instance = None  # class variable to store the instance created

    def __new__(cls, *args, **kwargs):
        """funcation to control the creation of object of class Singleton
        Returns:
            Singleton : instance of singleton object
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            print("instance created")

        return cls._instance


print("*" * 20)
print("creating S1")
# will print - instance created it is first instance
s1 = Singleton()
print(f"s1:{s1}")


print("*" * 20)
print("creating s2")
# will not create the instance. will share the allredy created instance
s2 = Singleton()
print(f"s2:{s2}")


# Both above variable will have the same memory address

# if there is relation between to classes, it is called the association. The association relation can be composition or aggregation


# Association

# public class Foo{
#     private Bar bar     # here Bar and Foo are associated.
# }


# composition   # Eg - House and Rooms


class Bar:
    def __init__(self):
        print("Bar is initialized")


class Foo:
    def __init__(self):
        self.bar = (
            Bar()
        )  # Here is Bar object is created with in the initialization of Foo Class. Bar object will die out once Foo object is killed.


foo = Foo()


# Aggregation   # Eg: Library and Books


class Bar1:
    def __init__(self) -> None:
        print("Bar1 object is created")


class Foo1:
    def __init__(self, bar1) -> None:
        self.bar1 = bar1  # here the bar object is created elsewhere but for the initialization of Foo object, bar object is required.
        # Bar object will continue to exist even after Foo object is killed


bar1 = Bar1()  # Bar object creation.
foo1 = Foo1(bar1)  # using all ready created bar object to initialize the Foo object

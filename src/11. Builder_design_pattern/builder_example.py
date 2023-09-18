class Door:
    pass


class Window:
    pass


class HouseType:
    type_1 = "DETACHED"
    type_2 = "SEMI_DETACHED"
    type_3 = "TERRACED"
    type_4 = "BUNGLOW"


class House:
    def __init__(self, house_type, door=None, window=None, roof=None):
        self.house_type = house_type
        self.door = door
        self.window = window
        self.roof = roof
        """
         ....
         ....
         ....
         ....
         ....
         
        lot many properties are required to build the house
        """

    def __str__(self) -> str:
        str = ""
        for k, v in self.__dict__.items():
            str = f"{str}|{k}={v}"
        return str


class HouseBuilder:
    def __init__(self, house_type):
        self.house = House(house_type=house_type)

    def set_window(self, window):
        # you can add checking here. like if house type is type1, window of
        # window_type 1 is allowed
        self.house.window = window
        return self

    def set_door(self, door):
        # additinal check if required
        self.house.door = door
        return self

    """
    def ....
        .....
        
    other other builder method
    
    """

    def build(self):
        return self.house


if __name__ == "__main__":
    my_house = (
        HouseBuilder(HouseType.type_1).set_door(Door()).set_window(Window()).build()
    )

    print(my_house)

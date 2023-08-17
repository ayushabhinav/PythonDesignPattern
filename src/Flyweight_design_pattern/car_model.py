import weakref


class CarModel:
    _models = weakref.WeakValueDictionary()

    def __new__(cls, model_name, *args, **kwargs):
        model = cls._models.get(model_name, None)
        if model is None:
            model = super().__new__(cls, *args, **kwargs)
            cls._models[model_name] = model
        return model

    def __init__(
        self,
        model_name,
        air_bag=False,
        tilt=False,
        cruise_control=False,
        power_locks=False,
        alloy_wheel=False,
        usb_charger=False,
    ):
        if not hasattr(self, "initted"):
            self.model_name = model_name
            self.air_bag = air_bag
            self.tilt = tilt
            self.cruise_control = (cruise_control,)
            self.power_locks = (power_locks,)
            self.alloy_wheel = (alloy_wheel,)
            self.usb_charger = usb_charger

    def some_method(self, *args, **kwargs):
        pass
        # This method is used to perform the operation on Flyweight car model class


class Car:
    def __init__(self, model, color, serial):
        self.model = model
        self.color = color
        self.serial = serial

    def some_method(self, *args, **kwargs):
        return self.model.some_method(*args, **kwargs)
        # This call the some method in the flyweight CarModel class

    def other_method(self, *args, **kwargs):
        pass
        # native method for operation on car class


if __name__ == "__main__":
    dx = CarModel("DX")
    lx = CarModel(
        "LX", air_bag=True, cruise_control=True, power_locks=True, usb_charger=True
    )

    car1 = Car(dx, "Blue", 12345)
    car2 = Car(dx, "Black", 89456)
    car3 = Car(lx, "red", 45678)
    car1000 = Car(lx, "grey", 198357)

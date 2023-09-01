import datetime


# preexisting object
class AgeCalculator:
    def __init__(self, birthday: str):
        self.year, self.month, self.day = (int(x) for x in birthday.split("-"))

    def calculate_age(self, date: str):
        year, month, day = (int(x) for x in date.split("-"))

        age = year - self.year
        if (month, day) < (self.month, self.day):
            age -= 1

        return age


# This is the adapter class which does the conversion of date to use
# the Age Calcualtor object
class DateAgeAdapater:
    def _str_date(self, date):
        return date.strftime("%Y-%m-%d")

    def __init__(self, birthdate):
        birthdate = self._str_date(birthdate)
        self.age_calculator = AgeCalculator(birthdate)

    def get_age(self, date):
        date = self._str_date(date)
        age = self.age_calculator.calculate_age(date)
        return age


# Above can also ne implemented using inheritance
class AgeableDate(datetime.date):
    def split(self, split_char):
        return (self.year, self.month, self.day)


if __name__ == "__main__":
    birthdate = AgeableDate(1975, 6, 1)
    today = AgeableDate.today()

    age_calculator = AgeCalculator(birthdate)
    age = age_calculator.calculate_age(today)
    print(age)

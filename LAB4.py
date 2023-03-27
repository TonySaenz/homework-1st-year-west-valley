# This is a program to demonstrate two rectangles
import datetime


class Rectangle:  # Define a class - Rectangle
    def __init__(self, width=1.0, height=2.0):  # Constructor - Class initializer
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width * self.height


rect1 = Rectangle(4, 40)
rect2 = Rectangle(3.5, 35.7)

print("Rectangle 1:")
print("\tWidth:", rect1.width)
print("\tHeight:", rect1.height)
print("\tArea:", rect1.get_area())
print("\tPerimeter:", rect1.get_perimeter())

print("Rectangle 2:")
print("\tWidth:", rect2.width)
print("\tHeight:", rect2.height)
print("\tArea:", rect2.get_area())
print("\tPerimeter:", rect2.get_perimeter())

# This is a program to represent a company's stock


class Stock:  # Define a class - Stock
    def __init__(self, symbol, name, previous_closing_price, current_price):  # Constructor - Class initializer
        self.__symbol = symbol
        self.__name = name
        self.__previous_closing_price = previous_closing_price
        self.current_price = current_price

    def get_name(self):
        return self.__name

    def get_symbol(self):
        return self.__symbol

    def get_previous_closing_price(self):
        return self.__previous_closing_price

    def set_previous_closing_price(self, previous_closing_price):
        self. __previous_closing_price = previous_closing_price

    def get_current_price(self):
        return self.current_price

    def set_current_price(self, current_price):
        self.current_price = current_price

    def get_change_percent(self):
        return (self.current_price - self.__previous_closing_price) / self.__previous_closing_price * 100


stock = Stock("INTC", "Intel Corporation", 20.5, 20.35)
print("\nStock Name:", stock.get_name())
print("Stock Symbol:", stock.get_symbol())
print("Price Change Percentage:", stock.get_change_percent())

# This is a program that measures the execution time in milliseconds


class StopWatch:  # Define a class - StopWatch
    def __init__(self):  # Constructor - Class initializer
        self.__startTime = datetime.datetime.now()
        self.__endTime = self.__startTime

    def start(self):
        self.__startTime = datetime.datetime.now()

    def stop(self):
        self.__endTime = datetime.datetime.now()

    def getElapsedTime(self):
        elapsedTime = self.__endTime - self.__startTime
        return elapsedTime.total_seconds() * 1000


stopwatch = StopWatch()

total = 0
stopwatch.start()
for i in range(1, 1000001):
    sum += i
stopwatch.stop()

print("\nThe total is", total)
print("Elapsed time in milliseconds:", stopwatch.getElapsedTime())







from unittest.mock import Mock


# Car class I want to mock - because it is needed for testing but not to be tested
class Car:
    """A Car object has speed attribute and 2 methods: drive and stop"""

    def __init__(self):
        self.speed = 0

    def drive(self, speed):
        self.speed = speed
        return f'Car goes at {self.speed} KM/H'

    def stop(self):
        self.speed = 0
        return "Car stopped"


# Mock for Car will have the same attributes and methods

# create the car mock based on Car class
car_mock = Mock(spec=Car)


# set the mock with a parameterized function - drive
# prepare a function to replace Car.speed
def drive_mock(speed):
    return f'Car Mock goes at {speed} KM/H'


# set the function on the mock
car_mock.drive.side_effect = drive_mock

# set the mock with a non parameterized function - stop
car_mock.stop.return_value = "Car Mock stopped"

# error - can't set function out of spec
# car_mock.turn.return_value = "Car Mock turned"


# use the Car Mock
print(car_mock.drive(150))
print(car_mock.stop())

# set any attributes you want
car_mock.speed = 25
car_mock.color = "red"
print(car_mock.speed)
print(car_mock.color)

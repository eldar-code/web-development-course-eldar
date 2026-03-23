from locations import Location
from unittest.mock import Mock

location = Location()
location_mockup = Mock(spec=Location)

location_mockup.move_right.return_value = 1
location_mockup.move_left.return_value = 0
location_mockup.move_up.return_value = 1
location_mockup.move_down.return_value = 0
# location_mockup.move.return_value = 100 # error - method not in class spec

x = location_mockup.move_right()
print(x)

x = location_mockup.move_left()
print(x)

y = location_mockup.move_up()
print(y)

y = location_mockup.move_down()
print(y)

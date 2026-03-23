class Location:

    def __init__(self):
        self.x = 0
        self.y = 0

    def move_right(self):
        pass
        # self.x += 1
        # return self.x

    def move_left(self):
        pass
        # self.x -= 1
        # return self.x

    def move_up(self):
        pass
        # self.y += 1
        # return self.y

    def move_down(self):
        pass
        # self.y -= 1
        # return self.y

if __name__ == "__main__":
    location = Location()
    print(f"(x={location.x}, y={location.y})")
    location.move_right()
    location.move_right()
    location.move_right()
    location.move_down()
    location.move_down()
    print(f"(x={location.x}, y={location.y})")

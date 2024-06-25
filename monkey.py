class Monkey:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def move(self, direction, steps):
        if direction == "left":
            self.position -= steps
        elif direction == "right":
            self.position += steps
        print(f"{self.name} moved {direction} to position {self.position}")

class Banana:
    def __init__(self, position):
        self.position = position

    def check_if_reached(self, monkey_position):
        return self.position == monkey_position

# Initialize positions
monkey = Monkey("George", 0)
banana = Banana(10)

# Simulation loop
while not banana.check_if_reached(monkey.position):
    direction = "right"  # Monkey always moves towards the banana
    monkey.move(direction, 1)

print("The monkey has reached the banana!")

class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):

        if name == "side_a":
            if value <= 0:
                raise ValueError("Сторона має бути більше за 0")
        if name == "angle_a":
            if value <= 0 or value >= 180:
                raise ValueError("Кут має бути від 1 до 179")

            object.__setattr__(self, "angle_b", 180 - value)

        object.__setattr__(self, name, value)

rhombus = Rhombus(5, 60)

print(rhombus.side_a)
print(rhombus.angle_a)
print(rhombus.angle_b)

rhombus.angle_a = 100
print(rhombus.angle_a)
print(rhombus.angle_b)
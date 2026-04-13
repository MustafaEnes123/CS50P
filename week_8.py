class Torque:
    def __init__(self, f, d):
        self.f = f
        self.d = d
    def calculate(self):
        return self.f * self.d
t = Torque(float(input("Force: ")), float(input("Distance: ")))
print(f"Torque: {t.calculate()} N.m")

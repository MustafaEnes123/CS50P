def main():
    f = float(input("Force (N): "))
    d = float(input("Distance (m): "))
    calculated_torque = calculate_torque(f, d)
    print(f"Torque: {calculated_torque} N.m")
def calculate_torque(force, distance):
    return force * distance
if __name__ == "__main__":
    main()

def main():
    f = float(input("Force (N): "))
    d = float(input("Distance (m): "))
    calculated_torque = f * d
    print(f"Torque: {calculated_torque} N.m")
main()

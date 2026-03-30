def main():
    name = input("Who is calculating? ")
    force = input("Force (N): ")
    distance = input("Distance (m): ")
    torque = float(force) * float(distance)
    with open("torque_log.csv", "a") as file:
        file.write(f"{name},{torque}\n")
    print("Result saved to torque_log.csv")
if __name__ == "__main__":
    main()
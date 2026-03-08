def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            pass
def main():
    f = get_float("Force (N): ")
    d = get_float("Distance (m): ")
    print(f"Applied torque: {f * d} N.m")
main()

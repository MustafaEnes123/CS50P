torque_results = [10.5, 20.0, 5.2, 30.1]
rounded_results = [round(t, 1) for t in torque_results]
for i, torque in enumerate(rounded_results, start=1):
    print(f"Calculation {i}: {torque} N.m")

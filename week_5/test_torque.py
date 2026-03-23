from torque import calculate_torque

def test_positive_values():
    assert calculate_torque(10, 2) == 20.0
    assert calculate_torque(5.5, 2) == 11.0

def test_zero_values():
    assert calculate_torque(0, 100) == 0.0
    assert calculate_torque(50, 0) == 0.0

def test_negative_values():
    assert calculate_torque(-10, 2) == -20.0
    assert calculate_torque(-5, -2) == 10.0

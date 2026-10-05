from app import calculate_total, calculate_average, calculate_grade


def test_calculate_total():
    marks = [85, 78, 90]
    assert calculate_total(marks) == 253


def test_calculate_average():
    marks = [85, 78, 90]
    assert round(calculate_average(marks), 2) == 84.33


def test_calculate_grade():
    assert calculate_grade(95) == "A+"
    assert calculate_grade(85) == "A"
    assert calculate_grade(75) == "B"
    assert calculate_grade(65) == "C"
    assert calculate_grade(50) == "D"
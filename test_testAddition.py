import pytest
from testAddition import Calculations

class TestCalculations:

    @pytest.mark.parametrize("a, b, expected", [
        (8, 2, 10),
        (3, 7, 10),
        (-5, 5, 0),
        (0, 0, 0)
    ])
    def test_get_sum(self, a, b, expected):
        calculation = Calculations(a, b)
        assert calculation.get_sum() == expected, "Sum calculation is incorrect"

    @pytest.mark.parametrize("a, b, expected", [
        (8, 2, 6),
        (3, 7, -4),
        (-5, 5, -10),
        (0, 0, 0)
    ])
    def test_get_difference(self, a, b, expected):
        calculation = Calculations(a, b)
        assert calculation.get_difference() == expected, "Difference calculation is incorrect"



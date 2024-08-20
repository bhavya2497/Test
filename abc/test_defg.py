import pytest
from abc.defg import MultiplicationAndDivision
class TestMultiplicationAndDivision:
    @pytest.mark.parametrize("a, b, expected", [
        (8, 2, 16),
        (3, 7, 21),
        (-5, 5, -25),
        (0, 10, 0)
    ])
    def test_get_product(self, a, b, expected):
        multiplicatioanddivision = MultiplicationAndDivision(a, b)
        assert multiplicatioanddivision.get_product() == expected, "Product calculation is incorrect"
    @pytest.mark.parametrize("a, b, expected", [
        (8, 2, 4),
        (21, 7, 3),
        (-10, 5, -2)
    ])
    def test_get_quotient(self, a, b, expected):
        multiplicatioanddivision = MultiplicationAndDivision(a, b)
        assert multiplicatioanddivision.get_quotient() == expected, "Quotient calculation is incorrect"

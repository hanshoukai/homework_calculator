import pytest
from Calculator.calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a,b,expect", [
        (3, 5, 8), (-1, -2, -3), (100, 300, 400), (1.5, 2.5, 4)
    ], ids=["add_int", "add_minus", "add_bigint", "add_decimal"])
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (5, 2, 3), (-1, -2, 1), (100, 50, 50), (5, 2.5, 2.5)
    ], ids=["sub_int", "sub_minus", "sub_bigint", "sub_decimal"])
    def test_sub(self, a, b, expect):
        assert expect == self.calc.sub(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (5, 2, 10), (-1, -2, 2), (100, 50, 5000), (5, 2.5, 12.5)
    ], ids=["mul_int", "mul_minus", "mul_bigint", "mul_decimal"])
    def test_mul(self, a, b, expect):
        assert expect == self.calc.mul(a, b)

    @pytest.mark.parametrize("a,b,expect", [
        (3, 0, 0), (0, 1, 0), (4, 2, 2), (-8, -2, 4), (100, 2, 50), (7.5, 1.5, 5)
    ], ids=["div_zeroDivisionError", "div_0/1", "div_int", "div_minus", "div_bigint", "div_decimal"])
    def test_div(self, a, b, expect):
        assert expect == self.calc.div(a, b)

import pytest

from montycarlopithon import PiCalculatorPython


class Test_PyCalculatorPython:

    @pytest.fixture
    def pi_calc(self):
        pi_calc = PiCalculatorPython()
        pi_calc._set_seed(0)
        return pi_calc

    def test_empty_valid(self, pi_calc):
        assert pi_calc.pi == None
        assert pi_calc._xs_inside == []
        assert pi_calc._ys_inside == []
        assert pi_calc._xs_outside == []
        assert pi_calc._ys_outside == []

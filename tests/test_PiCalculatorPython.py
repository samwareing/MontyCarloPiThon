import pytest

from montycarlopithon import PiCalculatorPython


class Test_PyCalculatorPython:

    @pytest.fixture
    def pi_calc(self):
        pi_calc = PiCalculatorPython()
        pi_calc._set_seed(0)
        return pi_calc

    def test_empty_valid(self, pi_calc):
        assert pi_calc.pi_approximations == []
        assert pi_calc.coords_inside == []
        assert pi_calc.coords_outside == []
        assert pi_calc.get_pi() == 0
        assert pi_calc.get_number_of_iterations() == 0

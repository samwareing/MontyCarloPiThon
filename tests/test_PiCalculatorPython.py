import pytest

from montycarlopithon import PiCalculatorPython


class Test_PyCalculatorPython:

    @pytest.fixture
    def pi_calc(self):
        pi_calc = PiCalculatorPython()
        pi_calc._set_seed(0)
        yield pi_calc

    @pytest.fixture
    def run_4_seed_0(self):
        yield {
            "coords_inside": [
                (0.420571580830845, 0.25891675029296335),
                (0.5112747213686085, 0.4049341374504143),
                (0.7837985890347726, 0.30331272607892745)
            ],
            "coords_outside": [(0.8444218515250481, 0.7579544029403025)],
            "pi_approximations": [0.0, 2.0, 2.6666666666666665, 3.0],
            "pi": 3.0,
            "iterations": 4
        }

    def test_empty_valid(self, pi_calc):
        assert pi_calc.pi_approximations == []
        assert pi_calc.coords_inside == []
        assert pi_calc.coords_outside == []
        assert pi_calc.pi == 0
        assert pi_calc.iterations == 0

    def test_run_4_seed_0(self, pi_calc, run_4_seed_0):
        pi_calc.run(4)
        assert pi_calc.coords_inside == run_4_seed_0["coords_inside"]
        assert pi_calc.coords_outside == run_4_seed_0["coords_outside"]
        assert pi_calc.pi_approximations == run_4_seed_0["pi_approximations"]
        assert pi_calc.pi == run_4_seed_0["pi"]
        assert pi_calc.iterations == run_4_seed_0["iterations"]

    def test_get_random_xy_coordinates_seed_0(self, pi_calc, run_4_seed_0):
        x, y = pi_calc._get_random_xy_coordinates()
        assert x, y == (0.420571580830845, 0.25891675029296335)
        x, y = pi_calc._get_random_xy_coordinates()
        assert x, y == (0.5112747213686085, 0.4049341374504143)

    def test_is_inside_circle_seed_0_inside(self, pi_calc):
        assert pi_calc._is_inside_circle(0.1, 0.1) is True

    def test_is_inside_circle_seed_0_outside(self, pi_calc):
        assert pi_calc._is_inside_circle(0.9, 0.9) is False

    @pytest.fixture
    def pi_calc_preset(self):
        pi_calc_preset = PiCalculatorPython()
        pi_calc_preset.coords_inside = [(0, 0), (1, 1)]
        pi_calc_preset.coords_outside = [(0, 0)]
        yield pi_calc_preset

    def test_calculate_pi_preset(self, pi_calc_preset):
        approximate_pi = 4.0 * 2.0 / (2.0 + 1.0)
        assert pi_calc_preset._calculate_pi() == approximate_pi
        approximate_pi = 2.666_666_666_667
        assert pytest.approx(
            pi_calc_preset._calculate_pi(),
            1e-12
        ) == approximate_pi

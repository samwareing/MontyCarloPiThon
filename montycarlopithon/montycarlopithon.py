import random


class MontyCarloPiThon:
    '''
    A Monte Carlo Pi calculator.
    Allows successive Monte Carlo runs.
    This is not optimised for speed.
    '''

    def __init__(self) -> None:
        self.pi = None
        self._set_seed()
        self._xs_inside = []
        self._ys_inside = []
        self._xs_outside = []
        self._ys_outside = []

    def _set_seed(self, seed=None) -> None:
        random.seed(seed)

    '''
    Perform the monte carlo run and estimate Pi.
    This works by:
    Selecting a random x and y co-ordinate between 0 and radius 1.
    Determining whether this co-ordinate would be located within a radius length.
    The ratio of hits within a radius length to the total number of hits is 1/4 of the value of Pi.

    The number of hits inside is representative of the area within a quadrant of that circle: (pi*r**2)/4.
    Let this be A.
    The number of hits total is representative of the area within a square: r**2.
    Let this be B.
    ((pi*r**2)/4)/(r**2) = A/B
    pi = 4*A/B
    '''

    def run(self, iterations: int) -> None:
        '''Runs the Monte Carlo simulation'''
        for i in range(iterations):
            x, y = self._get_random_xy_coordinates()
            if self._is_inside_circle(x, y):
                self._xs_inside.append(x)
                self._ys_inside.append(y)
            else:
                self._xs_outside.append(x)
                self._ys_outside.append(y)
        self.pi = self._calculate_pi()

    def _get_random_xy_coordinates(self) -> tuple:
        return (random.uniform(0.0, 1.0), random.uniform(0.0, 1.0))

    def _is_inside_circle(self, x: float, y: float) -> bool:
        return x * x + y * y < 1.0

    def _calculate_pi(self) -> float:
        '''Formula for calculating Pi from hits in circle and total hits'''
        return 4.0 * float(len(self._xs_inside)) / float(
            len(self._xs_inside) + len(self._xs_outside))

import random


class PiCalculatorPython:
    '''
    A Monte Carlo Pi calculator.
    Allows successive Monte Carlo runs.
    This is not optimised for speed.
    '''

    def __init__(self) -> None:
        self.pi_approximations = []
        self.coords_inside = []
        self.coords_outside = []
        self._set_seed()

    def _set_seed(self, seed=None) -> None:
        '''Allows setting your custom seed.'''
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
        '''Run Monte Carlo approximation of Pi'''
        for i in range(iterations):
            x, y = self._get_random_xy_coordinates()
            if self._iscoords_inside_circle(x, y):
                self.coords_inside.append((x, y))
            else:
                self.coords_outside.append((x, y))
            self.pi_approximations.append(self._calculate_pi())

    def _get_random_xy_coordinates(self) -> tuple:
        return (random.uniform(0.0, 1.0), random.uniform(0.0, 1.0))

    def _iscoords_inside_circle(self, x: float, y: float) -> bool:
        return x * x + y * y < 1.0

    def _calculate_pi(self) -> float:
        '''Formula for calculating Pi from hits in circle and total hits'''
        return 4.0 * float(len(self.coords_inside)) / float(
            len(self.coords_inside) + len(self.coords_outside))

    def get_pi(self) -> float:
        if self.pi_approximations:
            return self.pi_approximations[-1]
        else:
            return 0.0

    def get_number_of_iterations(self) -> int:
        return len(self.pi_approximations)

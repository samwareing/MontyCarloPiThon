import random
from math import sqrt


class MontyCarloPiThon:
    '''
    A Monte Carlo Pi calculator.
    Allows successive Monte Carlo runs.
    This is not optimised for speed.
    '''

    def __init__(self) -> None:
        self._hits_in_circle = 0
        self._hits_total = 0
        self.pi = None
        self._set_seed()

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
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            if sqrt(x * x + y * y) < 1.0:
                self._hits_in_circle += 1
        self._hits_total += iterations

        self.pi = self._calculate_pi(self._hits_in_circle, self._hits_total)

    def _calculate_pi(self, hits_in_circle: float, hits_total: float) -> float:
        '''Formula for calculating Pi from hits in circle and total hits'''
        return 4.0 * float(hits_in_circle) / float(hits_total)

    # def str(self):
    #     string = f'MonteCarloPiThon: '
    #     string += f'Pi: {self.pi}, '
    #     string += f'{self._hits_in_circle}/{self._hits_total} (in/to)'
    #     return string

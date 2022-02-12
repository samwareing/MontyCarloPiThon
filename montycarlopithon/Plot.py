import matplotlib.pyplot as plt
import math
from montycarlopithon import PiCalculatorPython


class Plot:
    def __init__(self, calculator, style='fast', figsize=(15, 10)):
        if not isinstance(calculator, (PiCalculatorPython)):
            raise TypeError("calculator must be a pi calculator.")
        self.calculator = calculator
        self._set_up_figure(style, figsize)
        self._add_text()
        self._create_hits_axs()
        self._create_convergence_axs()
        self._create_error_axs()

    def _set_up_figure(self, style, figsize) -> None:
        plt.style.use(style=style)
        self.figure = plt.figure(figsize=figsize)
        gridsize = (2, 3)
        self.hits_axs = plt.subplot2grid(
            gridsize,
            (0, 0),
            colspan=2,
            rowspan=2,
            aspect='equal'
        )
        self.convergence_axs = plt.subplot2grid(gridsize, (0, 2))
        self.error_axs = plt.subplot2grid(gridsize, (1, 2))

    def _add_text(self) -> None:
        title_size = 36
        subplot_title_size = 32
        label_size = 20
        self.figure.suptitle('Monty Carlo Pi Thon', fontsize=title_size)
        self.hits_axs.set_title(
            'Hits inside vs outside circle', fontsize=subplot_title_size)
        self.hits_axs.set_xlabel('x value', fontsize=label_size)
        self.hits_axs.set_ylabel('y value', fontsize=label_size)
        self.convergence_axs.set_title(
            'Convergence', fontsize=subplot_title_size)
        self.convergence_axs.set_xlabel('Iterations', fontsize=label_size)
        self.convergence_axs.set_ylabel(
            'Approximation Pi value', fontsize=label_size)
        self.error_axs.set_title('Error', fontsize=subplot_title_size)
        self.error_axs.set_xlabel('Iterations', fontsize=label_size)
        self.error_axs.set_ylabel('Error', fontsize=label_size)

    def _create_hits_axs(self):
        self._scatter_plot(self.calculator.coords_inside, color='red')
        self._scatter_plot(self.calculator.coords_outside, color='gray')

    def _scatter_plot(self, coords, color) -> None:
        self.hits_axs.scatter(
            [coord[0] for coord in coords],
            [coord[1] for coord in coords],
            c=color,
            marker='.'
        )

    def _create_convergence_axs(self):
        self.convergence_axs.semilogx(
            self.calculator.pi_approximations, color='red')
        self.convergence_axs.axhline(math.pi, color='gray')

    def _create_error_axs(self):
        N = self.calculator.iterations
        self.error_axs.loglog(
            range(N),
            [x-math.pi for x in self.calculator.pi_approximations]
        )
        self.error_axs.loglog([1/math.sqrt(i) for i in range(1, N+1)])


def main():
    pc = PiCalculatorPython()
    pc.run(999999)
    pass
    p = Plot(pc)
    print("ending")


if __name__ == "__main__":
    main()

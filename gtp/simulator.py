import numpy as np
import matplotlib.pyplot as plt
from gtp import GTPEstimator

def simulate(max_val, num_trials, num_iters, plot_confidence=True):
    iters = [i for i in range(num_iters)]

    for t in range(num_trials):
        guesses = []
        los = []
        his = []
        g = GTPEstimator([])
        for _ in range(num_iters):
            o = np.random.uniform(low=0, high=max_val)
            g.add_observation(o)
            est = g.estimate_maximum()
            lo,hi = g.get_confidence_intervals()
            guesses.append(est)
            los.append(lo)
            his.append(hi)

        if plot_confidence:
            plt.fill_between(iters, los, his, color='b', alpha=.1)
        else:
            plt.plot(iters, guesses)

    plt.plot([0, num_iters - 1], [max_val, max_val], c='r', linestyle='--', linewidth=3)

    plt.show()
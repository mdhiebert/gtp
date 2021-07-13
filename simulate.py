from gtp import GTPEstimator
from gtp.simulator import simulate
import argparse

parser = argparse.ArgumentParser('A simulator to demonstrate the performance of this estimator.')
parser.add_argument('--max_val', default=150, help='The ground-truth maximum value of this distribution. Default is 150.')
parser.add_argument('--num_trials', default=10, help='The number of trials (different experiments) to run. Default is 10.')
parser.add_argument('--num_iters', default=20, help='The number of observations to make in each trial. Default is 20.')
parser.add_argument('--conf_bounds', default=False, action='store_true', help='Whether or not to display the confidence intervals of our estimates.')
args = parser.parse_args()

simulate(args.max_val, args.num_trials, args.num_iters, args.conf_bounds)




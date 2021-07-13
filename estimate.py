import argparse
from gtp import GTPEstimator

def round_to_int(i):
    return int(round(i))

parser = argparse.ArgumentParser(description='')
parser.add_argument('--filename', type=str,
                    help='the .txt file containing a list of serial numbers')

args = parser.parse_args()
g = GTPEstimator.from_txt(args.filename)

est_max = g.estimate_maximum()
est_intvls = g.get_confidence_intervals()

print(f'Estimated Maximum: {round_to_int(est_max)} (raw is {est_max}) | 95% confidence bounds: {est_intvls}')

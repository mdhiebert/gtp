# GTP - German Tank Problem Estimator

A Python implementation of the estimator used in the [German Tank Problem](https://en.wikipedia.org/wiki/german_tank_problem).

- [Quickstart](#quickstart)
- [Example](#example)
- [Commands](#commands)

## Quickstart

1. Set up your environment with the following commands:

```
conda env create -f environment.yaml
conda activate gtp
```

2. Navigate to `gtp/`

3. Execute the following:

```
python estimate.py --filename <filename>
```

where `filename` is a `.txt` file that looks something like this:

```
<observation1>
<observation2>
<observation3>
<observation4>
...
<observationN>
```

where `<observationN>` is the N-th observed serial number, this should be an integer value. The ordering of this `.txt` file does not matter for this particular estimation strategy.


## Example

Say we have observed five serial numbers: 25, 26, 22, 84, and 69. We would format our file `test.txt` as follows:

```
25
26
22
84
69
```

and then in terminal run the command above to get our estimate:

```
$ python estimate.py --filename test.txt
Estimated Maximum: 100 (raw is 99.8) | 95% confidence bounds: (84, 152.92739305419073)
```

One month later, we identify five more numbers: 87, 92, 95, 96, 99. We add these to our text file:

```
25
26
22
84
69
87
92
95
96
99
```

We again run our estimator:
```
$ python estimate.py --filename test.txt
Estimated Maximum: 108 (raw is 107.9) | 95% confidence bounds: (99, 133.57900191968278)
```

So if one month ago, we estimated that they had 100, and we now estimate they have 108, we can reasonably infer that the production rate is roughly 108. So on and so forth...

## Commands

There are two supported scripts: `estimate.py` and `simulate.py`. The estimation script ingests `.txt` files and outputs estimates. The simulation script is more of a sanity check to show the efficacy of this method, and can be used to visualize the results of this estimator in simulation.

The help menu for `estimate.py`:
```python
$ python estimate.py -h
usage: estimate.py [-h] [--filename FILENAME]

optional arguments:
  -h, --help           show this help message and exit
  --filename FILENAME  the .txt file containing a list of serial numbers
```

The help menu for `simulate.py`:

```python
$ python simulate.py -h
usage: A simulator to demonstrate the performance of this estimator.
       [-h] [--max_val MAX_VAL] [--num_trials NUM_TRIALS]
       [--num_iters NUM_ITERS] [--conf_bounds]

optional arguments:
  -h, --help            show this help message and exit
  --max_val MAX_VAL     The ground-truth maximum value of this distribution.
                        Default is 150.
  --num_trials NUM_TRIALS
                        The number of trials (different experiments) to run.
                        Default is 10.
  --num_iters NUM_ITERS
                        The number of observations to make in each trial.
                        Default is 20.
  --conf_bounds         Whether or not to display the confidence intervals of
                        our estimates.
```
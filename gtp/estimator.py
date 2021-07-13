import math

class GTPEstimator:

    @staticmethod
    def from_txt(filename):

        with open(filename, 'r') as f:
            raw_data = f.read()
            lines = raw_data.split('\n')

        # convert every line to an integer and
        # ignore empty lines (empty strings)
        observations = [int(line) for line in lines if line]

        return GTPEstimator(observations)


    def __init__(self, obs):
        self.obs = [o for o in obs]
        self._update_internals()

    def _update_internals(self):
        self._k = len(self.obs)
        if self._k: self._m = max(self.obs)

    def add_observations(self, o_arr):
        '''
            Add a set of new observation to our set of observations.

            Parameters
            ----------
            obs_arr :: list[float | int] :
                a list of observed values
        '''

        self.obs.extend(o_arr)
        self._update_internals()

    def add_observation(self, o):
        '''
            Add a single new observation to our set of observations.

            Parameters
            ----------
            o :: float | int :
                an observed value
        '''
        self.obs.append(o)
        self._update_internals()

    def estimate_maximum(self, method = 'freq'):
        '''
            Estimate the maximum value of our population given observed samples.

            Parameters
            ----------
            method :: str{'freq' | 'bayes_med' | 'bayes_mean'} :
                the method with which to calculate the maximum of this population
        '''

        if self._k == 0: raise RuntimeError('No observed samples!')

        if method == 'freq':
            N_hat = self._m * (1 + (1 / self._k)) - 1
        elif method == 'bayes_med':
            N_hat = self._m + ((self._m * math.log(2)) / (self._k - 1))
        elif method == 'bayes_mean':
            N_hat = (self._m - 1) * ((self._k - 1) / (self._k - 2))
        else:
            raise RuntimeError('Invalid method for estimation.')

        return N_hat

    def get_confidence_intervals(self):
        '''
            Returns the 95% confidence interval as a tuple of (lower bound, upper bound)
        '''
        if self._k == 0: raise RuntimeError('No observed samples!')

        lower_bound = self._m
        upper_bound = self._m * (20 ** (1 / self._k))

        return (lower_bound, upper_bound)
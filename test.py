from gtp import GTPEstimator
import unittest

class GTPTest(unittest.TestCase):

    def _evaluate_wikipedia_answers(self, g):
        self.assertAlmostEqual(g.estimate_maximum('freq'), 74, places=0)
        self.assertAlmostEqual(g.estimate_maximum('bayes_med'), 74, places=0) # wiki is wrong according to their own math
        self.assertAlmostEqual(g.estimate_maximum('bayes_mean'), 89, places=0)


    def test_wikipedia_example(self):
        # https://en.wikipedia.org/wiki/German_tank_problem#Example
        obs = [19, 40, 42, 60]
        g = GTPEstimator(obs)
        self._evaluate_wikipedia_answers(g)


    def test_wikipedia_sequential_add(self):
        g = GTPEstimator([])

        g.add_observation(19)
        g.add_observation(40)
        g.add_observation(42)
        g.add_observation(60)

        self._evaluate_wikipedia_answers(g)

    def test_wikipedia_bulk_add(self):
        g = GTPEstimator([])
        obs = [19, 40, 42, 60]

        g.add_observations(obs)

        self._evaluate_wikipedia_answers(g)

if __name__ == '__main__':
    unittest.main()
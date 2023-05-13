import unittest
import sys
from projects.discrete.discretevar import Bernoulli, Binomial, Geometric, Poisson

SUCCESS = 1
FAIL = 0
sys.path.append("/simulacion_y_modelos/projects")

class BernoulliTest(unittest.TestCase):
    def test_basket_player(self):
        """
        A basketball player can shoot a ball into the basket with a probability of 0.6. What is the probability that he misses the shot?
        """
        probability = 0.6
        miss = FAIL
        answer = 0.4
        bernoulli = Bernoulli(probability= probability)
        
        self.assertEqual(bernoulli.density_function(miss), answer)
        
    def test_mean(self):
        """
        If a Bernoulli distribution has a parameter 0.45 then find its mean.
        """
        probability = 0.45
        answer = probability
        bernoulli = Bernoulli(probability= probability)
        
        self.assertEqual(bernoulli.mean(), answer)
        
    def test_variance(self):
        """
        If a Bernoulli distribution has a parameter 0.72 then find its variance.
        """
        probability = 0.72
        answer = 0.2016
        bernoulli = Bernoulli(probability=probability)
        
        self.assertEqual(bernoulli.variance(), answer)

class BinomialTest(unittest.TestCase):
    def test_coin_two_heads(self):
        """
        If a coin is tossed 5 times, find the probability of exactly 2 heads
        """
        probability = 0.5
        n = 5
        x = 2
        answer = 5/16
        binomial = Binomial(probability=probability, experiment_number=n)
        
        self.assertEqual(binomial.density_function(x), answer)
    
    def test_mean(self):
        """
        If a coin is tossed 5 times, then find the mean.
        """
        probability = 0.5
        n = 5
        answer = 2.5
        binomial = Binomial(probability=probability, experiment_number=n)
        
        self.assertEqual(binomial.mean(), answer) 
    
    def test_variance(self):
        """
        If a coin is tossed 5 times, then find the variance.
        """
        probability = 0.5
        n = 5
        answer = 1.25
        binomial = Binomial(probability=probability, experiment_number=n)
        
        self.assertEqual(binomial.variance(), answer)
        
class GeometricTest(unittest.TestCase):
    def test_win_darts_with_three_plays(self):
        """
        Suppose you are playing a game of darts. The probability of success is 0.4. 
        What is the probability that you will hit the bullseye on the third try?
        """
        probability = 0.4
        times_played = 3
        answer = 0.144
        geometric = Geometric(probability=probability, success_number=times_played)
        
        self.assertEqual(geometric.density_function(), answer)
    
    def test_mean(self):
        """
        If a patient is waiting for a suitable blood donor and the probability that the selected donor will be a match is 0.2, 
        then find the expected number of donors who will be tested till a match is found including the matched donor.
        """
        probability = 0.2
        answer = 5
        geometric = Geometric(probability=probability, success_number=0)
        
        self.assertEqual(geometric.mean(), answer)
    
    def test_variance(self):
        """
        With the previous example, find the variance.
        """
        probability = 0.2
        answer = 20
        geometric = Geometric(probability=probability, success_number=0)
        
        self.assertAlmostEqual(geometric.variance(), answer)

class PoissonTest(unittest.TestCase):
    def test_five_customer_per_minute(self):
        """
        In a cafe, the customer arrives at a mean rate of 2 per min. 
        Find the probability of arrival of 5 customers in 1 minute using the Poisson distribution formula.
        """
        mean = 2
        waited = 5
        answer = 0.036
        poisson = Poisson(ocurrencies_number=waited, lamb=mean)
        
        self.assertAlmostEqual(poisson.density_function(), answer, places=3)
        
    def test_mean(self):
        """
        With the previous example, find the mean.
        """
        mean = 2
        waited = 5
        answer = 2
        poisson = Poisson(ocurrencies_number=waited, lamb=mean)
        
        self.assertEqual(poisson.mean(), answer)
        
    def test_variance(self):
        """
        With the previous example, find the variance.
        """
        mean = 2
        waited = 5
        answer = 2
        poisson = Poisson(ocurrencies_number=waited, lamb=mean)
        
        self.assertEqual(poisson.variance(), answer)
        
if __name__ == "__main__":
    unittest.main()
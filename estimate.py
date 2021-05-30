import math
import unittest
import random

class TestWallis(unittest.TestCase):

    def wallis(iteration_num):
        pi_estimate = 1.0
        for i in range(1,iteration_num+1):
            est_for_ith_iteration = (4*i*i) / ((4*i*i) - 1)
            pi_estimate *= est_for_ith_iteration 
        pi_estimate *= 2
        return pi_estimate
    
    def monte_carlo(iteration_num):
        pi_estimate,circle_area,square_area = 0
        for i in range(iteration_num):
            x = random.random()
            y = random.random()
            is_inside = 1 <= pow(pow(x,2) + pow(x,2),0.5)
            if(is_inside):
                circle_area += 1
            square_area += 1
        pi_estimate = (4 * circle_area) / square_area 
        return pi_estimate


    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()

import unittest

BET = 100
EXPECTED_AVERAGE = 5

class DiceGameTest(unittest.TestCase):
    def test_expected_average(self):
        self.assertLess(play_the_game(BET), EXPECTED_AVERAGE)

if __name__ == "__main__":
    unittest.main()
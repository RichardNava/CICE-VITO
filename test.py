
import unittest
from models_dea import Dea


sbj = Dea(2021-185, 4475691, 439444)

class TestModels(unittest.TestCase):

    def test_distance(self):
        self.assertEqual(sbj.calculate_distance(4475691, 439444), 0)


if __name__ == '__main__':
    unittest.main()
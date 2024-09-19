import unittest
import pandas as pd
from rightsizer import Rightsizer

class TestRightsizer(unittest.TestCase):

    def setUp(self):
        data = {
            'instance_id': ['i-123', 'i-456'],
            'cpu_usage': [10, 80],
            'memory_usage': [25, 90]
        }
        self.usage_data = pd.DataFrame(data)
        self.rightsizer = Rightsizer(self.usage_data)

    def test_recommend_rightsizing(self):
        recommendations = self.rightsizer.recommend_rightsizing()
        self.assertEqual(recommendations['instance_id'].iloc[0], 'i-123')

if __name__ == '__main__':
    unittest.main()

"""
Unit tests for AWSDataCollector
"""
import unittest
from data_collector.aws_collector import AWSDataCollector

class TestAWSDataCollector(unittest.TestCase):
    
    def setUp(self):
        self.collector = AWSDataCollector()
    
    def test_get_ec2_instances(self):
        data = self.collector.get_ec2_instances()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 0)

    def test_get_s3_buckets(self):
        data = self.aws_collector.get_s3_buckets()
        self.assertIsInstance(data, list)

if __name__ == '__main__':
    unittest.main()

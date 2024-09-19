import unittest
from web_dashboard.app import app

class TestWebDashboard(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Cloud Cost Optimization Dashboard", response.data)

    def test_report_download(self):
        response = self.app.get('/download_report')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

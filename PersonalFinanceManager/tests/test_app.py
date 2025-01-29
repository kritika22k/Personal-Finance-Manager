import unittest
from app import create_app, db

class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_generate_report_page(self):
        response = self.client.post('/report', data={'name': 'Test', 'data': 'Sample data'})
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission

if __name__ == '__main__':
    unittest.main()

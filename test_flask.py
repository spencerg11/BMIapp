import unittest
from flask import Flask
from flask_testing import TestCase
from werkzeug.datastructures import ImmutableMultiDict
from processing import calculate_bmi, get_bmi_category

# Import your Flask application
from flask_app import app

class TestFlaskApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_calculate_page(self):
        with self.app.test_client() as client:
            response = client.post('/', data=ImmutableMultiDict([
                ('Weight_in_Lbs', '150'),
                ('Height_in_Feet', '5'),
                ('Inches', '9')
            ]))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Your BMI is', response.data)

if __name__ == '__main__':
    unittest.main()

""" Tests for views.py """
from app import app
import unittest
import json


class TestRouteCases(unittest.TestCase):
    """ Test Cases """
    def setUp(self):
        """ Instantiate test client """
        self.app = app.test_client()  # test client
        # Sample user data
        self.sample = {
            'username': 'artorious',
            'email': 'arthurngondo@email.com',
            'password': 123454321,
            'confirm_password': 123454321,
            'first_name': 'Arthur',
            'last_name': 'Ngondo'
            }

    def test_register_status(self):
        """ Test endpoint sends HTTP POST request to the application."""
        result = self.app.post(
            '/api/v1/register',
            data=json.dumps(self.sample),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(result.status_code, 201)

    def test_register_Success_operation_message(self):
        """ Test endpoint returns message to user to indicate Pass/Fail """
        result = self.app.post(
            '/api/v1/register',
            data=json.dumps(self.sample),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(result.data, 'Success!')

    def test_register_handles_bad_request(self):
        """ Test for returns message to user to indicate Bad request - 404 """
        result = self.app.post(
            '/api/v1/registerss',
            data=json.dumps(self.sample),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(
            'Resource NOT Found. Account NOT created',
            str(result.data)
        )

if __name__ == '__main__':
    unittest.main()
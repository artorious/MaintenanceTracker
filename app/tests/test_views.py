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
        
        self.sample_bad = {
            'username': '',
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
        self.assertIn(b'Account Registered', result.data)

    def test_register_handles_bad_request(self):
        """ Test for returns message to user to indicate Bad request - 404 """
        result = self.app.post(
            '/api/v1/registerss',
            data=json.dumps(self.sample),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(
            404,
            result.status_code,
            msg='Resource NOT Found. Account NOT created'
        )

    def test_for_valid_data_in_payload(self):
        """ Tests that user has inputted all relevant
            data into the payload before posting.
        """
        result = self.app.post(
            '/api/v1/register',
            data=json.dumps(self.sample_bad),
            headers={'content-type': 'application/json'}
        )
        self.assertIn(b'Registration Failed', result.data)

if __name__ == '__main__':
    unittest.main()

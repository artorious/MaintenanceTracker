""" Tests for models.py """
from app.models import Users
import unittest


class TestUsersClass(unittest.TestCase):
    """ Test Cases """

    def setUp(self):
        """ Instantiate test client """
        self.sample_user = Users()
        self.sample = {
            'username': 'artorious',
            'email': 'arthurngondo@email.com',
            'password': 123454321,
            'confirm_password': 123454321,
            'first_name': 'Arthur',
            'last_name': 'Ngondo'
            }

    def test_users_class_inits_with_dict(self):
        """ Test that Users class initializes with an empty dict. """
        self.assertDictEqual(
            {}, self.sample_user,
            'Class does not initailze an empty dict'
        )

    def test_users_class_inits_with_appropririate_login_status(self):
        """ Test that Users class initializes with a login status of False
            (logged off)
        """
        self.assertEqual(False, self.sample_user.login_status)

    def test_register_packs_params_into_dict(self):
        """ Test register method inserts provided params into a dict """
        result = self.sample_user.register(
            'arthurngondo@email.com',
            'artorious',
            'Arthur',
            'Ngondo',
            123454321,
            123454321)
        self.assertIn('Account Registered', result)

    def test_register_handles_existing_username(self):
        """ Tests for an already registered username
            before appending to dictionary
        """
        result1 = self.sample_user.register(
            'ngondo@email.com',
            'artorious',
            'Arthurs',
            'Ngondoz',
            12345432156,
            12345432156)
        
        result2 = self.sample_user.register(
            'arthurngondo@email.com',
            'artorious',
            'Arthur',
            'Ngondo',
            123454321,
            123454321)
        self.assertIn(
            'Username Already in Use. Try a different name.',
            result2)
    
    def test_register_handles_existing_email(self):
        """ Tests for an already registered email
            before appending to dictionary
        """
        result1 = self.sample_user.register(
            'arthurngondo@email.com',
            'artorious',
            'Arthurs',
            'Ngondoz',
            12345432156,
            12345432156)
        
        result2 = self.sample_user.register(
            'arthurngondo@email.com',
            'ngondez',
            'Arthur',
            'Ngondo',
            123454321,
            123454321)
        self.assertIn(
            'Email Already registered. Try a different name.',
            result2)

    def test_register_handles_inconsistent_passwords(self):
        """ Tests that register function handles miss-matched passwords """
        result = self.sample_user.register(
            'arthurngondo@email.com',
            'artorious',
            'Arthur',
            'Ngondo',
            1234543213,
            1234543214)
        self.assertIn('Password Does not match - Try again', result)

if __name__ == '__main__':
    unittest.main()

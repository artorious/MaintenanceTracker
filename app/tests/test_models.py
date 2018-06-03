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

    def test_users_class_inits_with_dicts(self):
        """ Test that Users class initializes with an empty dicts. """
        self.assertDictEqual(
            {}, self.sample_user.user_account,
            'Class does not initailze an empty dict'
        )
        self.assertDictEqual(
            {}, self.sample_user.all_requests,
            'Class does not initailze an empty dict'
        )

    def test_users_class_inits_with_appropririate_login_status(self):
        """ Test that Users class initializes with a login status of False
            (logged off)
        """
        self.assertFalse(self.sample_user.login_status)

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
        result = self.sample_user.register(
            'ngondo@email.com',
            'artorious',
            'Arthurs',
            'Ngondoz',
            12345432156,
            12345432156)
        
        result = self.sample_user.register(
            'arthurngondo@email.com',
            'artorious',
            'Arthur',
            'Ngondo',
            123454321,
            123454321)
        self.assertIn(
            'Username Already in Use. Try a different name.',
            result)

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

    def test_signout_returns_message(self):
        """ Tests for Logging out message """
        self.assertEqual(self.sample_user.logout(), "You have been SIGNED OUT")


if __name__ == '__main__':
    unittest.main()

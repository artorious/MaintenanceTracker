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
        

if __name__ == '__main__':
    unittest.main()

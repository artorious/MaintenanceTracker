""" Data representation for Maintenance Web App

    Holds routines for users to interact with the API
"""


class Users(dict):
    """ Holds methods for users

        Attributes:
            user_account (dict) - Holds all user account details and requests
            associated with the account.
            login_status (bool) - True/False flag to indicate wheteher or not a
            is logged on.
            all_requests (dict) - Holds all requests by users
            current_user - Holds username of currently logged user
    """

    def __init__(self):
        self.user_account = {}
        self.login_status = False
        self.all_requests = {}
        self.current_user = None
        self.request_counter = 1
 
    # GET: /api/v1/users/login
    def login(self, username, password):
        """(Users, str, str) -> str

            Logs in a registered user.
            Returns 'Success' or 'Fail' message

            TODO: authenticate user credentials
            TODO: Return msg to user 'Success/Fail
        """
        pass

    # POST: /api/v1/users/logout
    def logout(self):
        """(Users) -> str

            Logs out a user and returns message.
        """
        self.login_status = False
        return "You have been SIGNED OUT"

    # POST: /api/v1/register
    def register(
            self, email, username, first_name, last_name, 
            password, confirm_password):
        """(Users, str, str, str, str, int, int) -> dict

            Creates a user account and stores user's information.
        """
        if password == confirm_password:
            if username in self.user_account.keys():
                return 'Username Already in Use. Try a different name.'
            else:
                self.user_account[username] = {}
                self.user_account[username]['email'] = email
                self.user_account[username]['first_name'] = first_name
                self.user_account[username]['last_name'] = last_name
                self.user_account[username]['password'] = password
                self.login_status = True
                self.current_user = username
                self.all_requests[self.current_user] = {}
                return 'Account Registered'
        else:
            return 'Password Does not match - Try again'

    # GET: /api/v1/users/requests
    def all_user_requests(self):
        """ (Users) -> str

            Fetches all requests associated with a username and displays them
        """
        return self.all_requests[self.current_user]
    
    # GET: /api/v1/users/requests/<requestID>
    def request_expanded(self, requestID):
        """ (Users, int) -> str

            Fetches and displays all information associated with 
            the requestID provided

            TODO: Return/print requests to screen
        """
        if isinstance(requestID, int) and requestID <= self.request_counter:
            return self.all_requests[self.current_user][requestID]
        else:
            return 'Not Found'

    # POST: /api/v1/users/requests
    def create_request(self, request_description):
        """ (Users, str) -> str

        Adds/creates a new request. 
        Assigns a unique request_ID to keep track of the record.
        Returns 'Success' message
        """
        self.all_requests[self.current_user] = {
            self.request_counter: request_description
        }
        self.request_counter += 1
        return 'Request Added'

    # PUT: /api/v1/users/requests/<requestID>
    def modify_request(self, requestID):
        """ (Users, int) -> str

            Updates the user request associated with the provided requestID
            Returns 'Success' or 'Fail' message
        """
        pass


def main():
    """ Dry run code """
    pass

if __name__ == '__main__':
    main()

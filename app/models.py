""" Data representation for Maintenance Web App

    Holds routines for users to interact with the API
"""


class Users(object):
    """ Holds methods for users

        Attributes:
    """

    def __init__(self):
        pass
    
    # GET: /api/v1/users
    def login(self, username, password):
        """(Users, str, str) -> str

            Logs in a registered user.
            Returns 'Success' or 'Fail' message

            TODO: authenticate user credentials
            TODO: Return msg to user 'Success/Fail
        """
        pass

    # GET: /api/v1/
    def logout(self):
        """(Users) -> str

            Logs out a user.
            Returns 'Success' or 'Fail' message.
            
            TODO: Return msg to user 'Success/Fail
        """
        pass

    # POST: /api/v1/register
    def register(
            self, email, username, first_name, last_name, 
            password, confirm_password):
        """(Users, str, str, str) -> str

            Creates a user account and stores user's information
            
            Returns 'Success' or 'Fail' message
            
            TODO: Return msg to user 'Success/Fail
        """
        pass
    
    # GET: /api/v1/requests
    def all_requests(self):
        """ (Users) -> str

            Fetches all requests associated with a username and displays them

            TODO: Return/print requests to screen
        """
        pass
    
    # GET: /api/v1/requests/<requestID>
    def request_expanded(self, requestID):
        """ (Users, int) -> str

            Fetches and displays all information associated with 
            the requestID provided

            TODO: Return/print requests to screen
        """
        pass

    # POST: /api/v1/requests
    def create_request(self):
        """ (Users) -> str

        Adds/creates a new request. 
        Assigns a unique request_ID to keep track of the record

        Returns 'Success' or 'Fail' message
        """
        pass

    # PUT: /api/v1/requests/<requestID>
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

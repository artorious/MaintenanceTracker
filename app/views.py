""" Routes for MaintenanceTracker App """
from flask import request, jsonify
from app.models import Users
from app import app

# Init
sample_account = Users()


@app.route('/api/v1/users/register', methods=['POST'])
def register():
    """ Register a new user and return message to user """
    req_data = request.get_json()

    if (
            'email' in req_data and
            'username' in req_data and
            'first_name' in req_data and
            'password' in req_data and
            'confirm_password' in req_data):

        reg_email = req_data['email']
        reg_username = req_data['username']
        reg_first_name = req_data['first_name']
        reg_last_name = req_data['last_name']
        reg_password = req_data['password']
        reg_conf_password = req_data['confirm_password']

        result = sample_account.register(
            reg_email,
            reg_username,
            reg_first_name,
            reg_last_name,
            reg_password,
            reg_conf_password
        )
        return jsonify(result), 201
    else:
        return jsonify('Registration Failed')


@app.route('/api/v1/users/signout', methods=['POST'])
def signout():
    """ Logs out a user and returns message to user. """
    return jsonify(sample_account.logout())


@app.route('/api/v1/users/requests', methods=['GET', 'POST'])
def requests():
    """ Fetches all the requests of a logged in user - GET
        Creates a new request - POST
    """
    if request.method == 'GET':
        return jsonify(sample_account.all_user_requests())
    else:
        req_data = request.get_json()
        return jsonify(sample_account.create_request(req_data))

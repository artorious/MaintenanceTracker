""" Routes for MaintenanceTracker App """
from flask import request, jsonify
from app.models import Users
from app import app

# Init
sample_account = Users()


@app.route('/api/v1/register', methods=['POST'])
def register():
    """Return msg to user - Success or Failed """
    req_data = request.get_json()
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

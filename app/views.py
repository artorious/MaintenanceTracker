""" Routes for MaintenanceTracker App """
from flask import request, jsonify
from app.models import Users
from app import app

# Init
sample_account = Users()


@app.route('/api/v1/register', methods=['POST'])
def register():
    """Return msg to user - Success or Failed """
    reg_email = request.get_json()
    reg_username = request.get_json()
    reg_first_name = request.get_json()
    reg_last_name = request.get_json()
    reg_password = request.get_json()
    reg_conf_password = request.get_json()

    result = sample_account.register(
        reg_email,
        reg_username,
        reg_first_name,
        reg_last_name,
        reg_password,
        reg_conf_password
        )
    return jsonify(result), 201

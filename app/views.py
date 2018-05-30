""" Routes for MaintenanceTracker App """
from flask import request
from app.models import Users
from app import app


@app.route('/api/v1/register', methods=['POST'])
def register():
    """Return msg to user - Success or Failed """
    pass

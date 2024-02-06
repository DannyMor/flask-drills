from flask import Blueprint, send_from_directory

api = Blueprint('api', __name__, url_prefix='/api/v1')


@api.route('/')
def index():
    return send_from_directory('static', 'index.html')

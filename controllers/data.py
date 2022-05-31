import json

from f1_types import DataRequest
from repositories.f1 import get_session
from services.chartify import fastest_laps
from flask import Blueprint, request, Response

data_controller = Blueprint('data_controller', __name__)


@data_controller.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        body = DataRequest(**request.get_json())
    if request.method == 'GET':
        body = DataRequest(int(request.args.get('year')),
                           int(request.args.get('track')),
                           request.args.get('session'),
                           request.args.get('drivers').split(','),
                           request.args.get('metrics').split(','))

    session_data = get_session(body)
    return Response(response=json.dumps(fastest_laps(body.drivers, session_data)),
                    status=200,
                    mimetype='application/json')

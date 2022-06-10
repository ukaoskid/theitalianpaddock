import json

from f1_types import DataRequest
from repositories.f1 import get_session
from services.chartify import fastest_laps, laps
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
    response = [
        fastest_laps(body.drivers, body.metrics, session_data),
        laps(body.drivers, session_data)
    ]

    return Response(response=json.dumps(response), status=200, mimetype='application/json')

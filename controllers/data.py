from f1_types import DataRequest
from repositories.f1 import get_session
from flask import Blueprint, request, Response

data_controller = Blueprint('data_controller', __name__)


@data_controller.route('/data', methods=['POST'])
def data():
    body = DataRequest(**request.get_json())
    session_data = get_session(body)
    return Response(response=session_data.laps[1].to_json(),
                    status=200,
                    mimetype='application/json')

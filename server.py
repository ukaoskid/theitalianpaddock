import flask
from flask_cors import CORS

from controllers.data import data_controller

app = flask.Flask(__name__)
CORS(app)

# Registering routes
app.register_blueprint(data_controller)
app.run()

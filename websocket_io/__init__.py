from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
app.config.from_envvar('WEBSOCKET_IO_SETTINGS', silent = True)

from views.default import default_view

app.register_blueprint(default_view)

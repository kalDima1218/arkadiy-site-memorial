import os
import hashlib
import pyqrcode
from flask_socketio import SocketIO
from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = False


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


#app.run(host="аркадий-держись.рф")
socketio = SocketIO()
socketio.init_app(app)
socketio.run(app, host="аркадий-держись.рф")
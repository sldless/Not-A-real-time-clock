from flask import Flask, render_template
from datetime import datetime
import requests
from flask_socketio import SocketIO
from flask.json import jsonify
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

def get_time() -> tuple:
    time = datetime.now()
    return (time.hour, time.minute, time.second)

@app.route('/')
def index():
    hour, minute, second = get_time()

    if (hour == 0):
        hour = 12
    elif (hour > 12):
        hour -= 12
    
    return render_template('index.html', hour=hour, minute=minute, second=second)

@app.route('/refresh_data')
def refresh_data():

    data = requests.get('http://127.0.0.1:5000/')
    return jsonify({'data': data.text})

if __name__ == '__main__':
    app.run(debug=True)
    socketio.run(app)

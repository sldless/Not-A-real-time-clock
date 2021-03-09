from flask import Flask, render_template
from datetime import datetime
import requests
from flask_socketio import SocketIO
from flask.json import jsonify
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

def get_time():
    time = datetime.now()
    hour = time.hour
    minute = time.minute
    second = time.second
    time_now = {"hour":hour, "minute": minute, "second": second}
    return time_now

@app.route('/')
def index():
    hour = get_time().get('hour')
    minute = get_time().get('minute')
    second = get_time().get('second')
    if (hour == 0):
        hour = 12
    if (hour > 12):
        hour = hour - 12
        
    if (minute < 10):
        minute = 0 + minute
    if (second  < 10):
        minute = 0 + second
        
    context = {
        'hour': hour,
        'minute': minute,
        'second': get_time().get('second')
    }
    context.update(**context)
    return render_template('index.html', **context)

@app.route('/refresh_data')
def refresh_data():

    data = requests.get('http://127.0.0.1:5000/')
    return jsonify({'data': data.text})

if __name__ == '__main__':
    app.run(debug=True)
    socketio.run(app)

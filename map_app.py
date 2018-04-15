"""
Put your Flask app code here.
"""

from flask import Flask
from flask import render_template
from flask import request
import plot_a_route
import weather_app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

def valid_login(firstname, lastname, email, username, password):
    if firstname == '':
        return False
    if lastname == '':
        return False
    if email == '':
        return False
    if username == '':
        return False
    if password == '':
        return False
    return True

def log_the_user_in(firstname, lastname):
    return render_template('profile.html', firstname=firstname, lastname=lastname)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['firstname'],
                        request.form['lastname'],
                        request.form['email'],
                        request.form['username'],
                        request.form['password']):
            with open('storeformdata.txt', 'w') as f:
                f.write(request.form['firstname'])
                f.write(request.form['lastname'])
                f.write(request.form['email'])
                f.write(request.form['username'])
                f.write(request.form['password'])
            return log_the_user_in(request.form['firstname'], request.form['lastname'])
        else:
            error = 'Missing required information'
    return render_template('error.html', error=error)

@app.route('/makemap', methods=['POST', 'GET'])
def make_map():
    plot_a_route.run(request.form['start'], request.form['distance'])
    return render_template('my_map.html')

@app.route('/weather', methods=['POST', 'GET'])
def post_weather():
    #todaysWeather = climate(request.form['place'])
    return render_template('map_app_weather.html')

if __name__ == '__main__':
    app.run()

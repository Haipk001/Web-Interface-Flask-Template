from flask import Flask, render_template, redirect, url_for, request, session
from waitress import serve
from flask_session import Session
from datetime import datetime

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['UPLOAD_FOLDER']='logs'
Session(app)

credentials = ('admin', 'admin')


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

@app.route('/')
def index():

    try:
        session["logged_in"] == True
    except KeyError:
        session["logged_in"] = False
    # nothing to show in the index, redirect to login page
    return redirect(url_for('login'))


@app.route('/login')
def login(alert="Login to continue...", alert_type="alert-primary"):
    # set default alert and alert type for login page
    if request.args.get('failed'):
        # if user has typed wrong credentials it reports as 'failed'
        alert = "Try again! Login failed..."
        alert_type = "alert-danger"
    elif request.args.get('invalid'):
        # if user tries to access welcome page with out logging in first reports 'invalid'
        alert = "Please login to continue..."
        alert_type = "alert-warning"
    
    if session['logged_in']:
        # if user is logged in only then render the home page
        return render_template('home.html')
    else:
        # otherwise take them to login page
        return render_template('login.html', alert=alert, alert_type=alert_type)


@app.route('/home')
def home():
    if session['logged_in']:
        # if user is logged in only then render the welcome page
        return render_template('home.html')
    else:
        # otherwise take them to login page
        return redirect(url_for('login', invalid="true"))


@app.route('/project')
def project():
    if session['logged_in']:
        # if user is logged in only then render the welcome page
        return render_template('project.html')
    else:
        # otherwise take them to login page
        return redirect(url_for('login', invalid="true"))


@app.route('/about')
def about():
    if session['logged_in']:
        # if user is logged in only then render the welcome page
        return render_template('about.html')
    else:
        # otherwise take them to login page
        return redirect(url_for('login', invalid="true"))


@app.route('/instruction', methods = ['GET'])
def instruction():
    return render_template('instruction.html')


@app.route('/validate', methods=['POST'])
def validate():
    if session['logged_in'] or request.form.get('username') == credentials[0] and request.form.get('password') == credentials[1]:
        # if user is logged in or they give in the correct credentials then take them to home page
        session['logged_in'] = True

        return redirect(url_for('home'))
    else:
        # if not logged in or they give wrong credentials take them to login page
        return redirect(url_for('login', failed='true'))


@app.route('/logout')
def logout():
    # logout method logs out the user and takes them back to login page
    session['logged_in'] = False
    return redirect(url_for('login'))

if __name__ == '__main__':
    #app.run(host = '127.0.0.1', port = 5000, debug = True)
    app.run(host = '0.0.0.0', port = 8080, debug = True)
    #serve(app, host='0.0.0.0', port=8080)
    #serve(app, host='127.0.0.1', port=5000)
    #serve(app, host='127.0.0.1', port=8080)


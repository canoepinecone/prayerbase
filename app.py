from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        # TODO: add login code
        return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        # TODO registration code
        return redirect(url_for('index'))

@app.route('/newprayer', methods=['GET', 'POST'])
def newprayer():
    if request.method == 'GET':
        return render_template('newprayer.html')
    elif request.method == 'POST':
        # TODO new prayer method
        return redirect(url_for('index'))

@app.route('/showprayer', methods=['GET'])
def showprayer():
    # TODO params in url
    return render_template('show.html')

app.run()
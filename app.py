from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Prayer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(500), unique=True)

    def __repr__(self):
        return '<Prayer %r>' % self.title

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(200))

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/', methods=['GET'])
def index():
    prayers = Prayer.query.all()
    return render_template('index.html', prayers=prayers)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        # TODO add login code
        return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        user = User(username = request.form['username'], password_hash = request.form['password'])
        db.session.add(user)
        db.session.commit()
        # TODO login registered user
        return redirect(url_for('index'))

@app.route('/newprayer', methods=['GET', 'POST'])
def newprayer():
    if request.method == 'GET':
        return render_template('newprayer.html')
    elif request.method == 'POST':
        prayer = Prayer(title = request.form['title'], description = request.form['description'], image_url = request.form['image'])
        db.session.add(prayer)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/showprayer', methods=['GET'])
def showprayer():
    # TODO params in url
    return render_template('show.html')

@app.route('/deleteprayer', methods=['GET'])
def deleteprayer():
    # TODO params in url
    return redirect(url_for('index'))

app.run()

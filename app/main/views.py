from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, LogoutForm, SignUpForm
from keychain import Keys

import json
import datetime as dt
import yfinance as yf
import pandas as pd

app = Flask(__name__, template_folder='../templates')
app.config['SECRET_KEY'] = Keys.secret()
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.create_all()

class Ticker(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    symbol = db.Column(db.String(10))
    
    ####### SAVE JUST IN CASE NEED TO CHANGE BACK ########
    # class Ticker(db.Model):
    # id = db.Column('id', db.Integer, primary_key=True)
    # symbol = db.Column(db.String(10))
    # current_price = db.Column(db.Float)
    # market_high = db.Column(db.Float)
    # market_low = db.Column(db.Float)
    # market_open = db.Column(db.Float)
    # market_close = db.Column(db.Float)

### TEST TO PRINT STOCK DATA ###
ticker = yf.Ticker('TSLA')
df = ticker.info
print(df)


##### DASHBOARD #####

@app.route("/dashboard")
def dashboard():
    ticker_list = Ticker.query.all()
    ticker = yf.Ticker('TSLA') # temporary.... how to pass 'symbol' from Ticker class?
    df = ticker.history(period="today")
    current_price = df['Close'] # Where do I get current price??? 
    market_high = df['High']
    market_low = df['Low']
    market_open = df['Open']
    market_close = df['Close']
    return render_template("dashboard.html", 
                           ticker_list=ticker_list, 
                           current_price=current_price, 
                           market_high=market_high, 
                           market_low=market_low,
                           market_open=market_open,
                           market_close=market_close)
    
# Add a new symbol to track in DB
@app.route("/add", methods=["POST"])
def add():
    symbol = request.form.get("symbol")
    new_ticker = Ticker(symbol=symbol)
    print(new_ticker)
    db.session.add(new_ticker)
    db.session.commit()
    return redirect('/dashboard')

# Delete a symbol being tracked in DB             
@app.route("/delete/<int:ticker_id>")   
def delete(ticker_id):
    Ticker.query.filter_by(id=ticker_id).delete()
    db.session.commit()
    return redirect('/dashboard')


##### SIGNUP #####

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()

    print('signup page accessed')
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data

        with open('app/main/user_data.json', mode='r') as file:
            data = json.load(file)

        with open('app/main/user_data.json', mode='w') as file:
            all_users = data['users']
            user_data = {
                'password': password,
                'email': email
            }
            user = {username: user_data}
            all_users.append(user)
            data = {"users":all_users}
            json.dump(data, file)

        return redirect('/login')

    return render_template('signup.html', form=form)


##### LOGIN #####

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Check user_data.json for username & password match
        with open('app/main/user_data.json', 'r') as file:
            data = json.load(file)
            all_users = data['users']

            for user in all_users:
                _username = list(user.keys())[0]
                if username == _username and password == user[_username]['password']:
                    return render_template('dashboard.html', form=LogoutForm(), display_message='Login Success')
        
            return render_template('login.html', form=form, display_message='Incorrect Login')

    return render_template('login.html', form=form, display_message='User Login')


##### PROFILE #####

@app.route('/profile/', methods=['GET', 'POST'])
def profile():
    form = LogoutForm()

    return render_template('profile.html', form=form)


##### LOGOUT #####

@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    form = LogoutForm()
    
    if form.validate_on_submit():

        return render_template('home.html', form=form, display_message='Successfully logged out')
    else:
        
        return render_template('profile.html')
    
    
#### HOME #####

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


##### RUN APP #####

if __name__=='__main__':
    app.run(debug=True)
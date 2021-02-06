from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email

class SignUpForm(FlaskForm):
    # Data fields that connect to inputs fields on signup.html in templates.
    username = StringField('Username', validators=[InputRequired(), Length(min=2, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=2, max=15)])
    #firstname = StringField('First Name')
    #lastname = StringField('Last Name')
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid Email'), Length(max=20)])
    stocks = StringField('stocks', validators=[ Length(min=2, max=5)])
    #phone = StringField('Phone')
    #address = StringField('Address')
    #addressLine2 = StringField('Address Line 2')
    #city = StringField('City')
    #state = StringField('State')
    #zipcode = StringField('Zip Code')
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired()])
    password = PasswordField(validators=[InputRequired()])
    submit = SubmitField('Login')

class UpdateForm(SignUpForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=2, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=2, max=15)])
    #firstname = StringField('First Name')
   # lastname = StringField('Last Name')
    email = StringField('Email')
    #phone = StringField('Phone')
    #address = StringField('Address')
    #addressLine2 = StringField('Address Line 2')
    #city = StringField('City')
    #state = StringField('State')
    #zipcode = StringField('Zip Code')
    update = SubmitField('Submit')

class LogoutForm(FlaskForm):
    logout = SubmitField('Submit')
from flask_wtf import FlaskForm
from wtforms import PasswordField,SubmitField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired,Email

class LoginForm(FlaskForm):
	username = EmailField('Email', validators = [DataRequired(), Email()], render_kw = {'placeholder' : 'Enter Username'})
	password = StringField('Password', validators = [DataRequired(message='Password required')], render_kw = {'placeholder' : 'Enter Password'})
	submit = SubmitField('Submit') 
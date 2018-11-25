from wtforms import Form, StringField, PasswordField, SubmitField, validators
from flask_wtf import FlaskForm 
class loginForm(FlaskForm):
    username = StringField(u'username', [validators.required(), validators.length(max=10)])
    password =  PasswordField(u'password',[validators.required()])
    submit = SubmitField(u'submit')

    class Meta:
        csrf = False


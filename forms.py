from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, validators, URLField

class LoginForm(FlaskForm):
    username = StringField('Username', [validators.InputRequired()])
    password = PasswordField('Password', [validators.InputRequired()])
    submit = SubmitField("Login")

class LegoForm(FlaskForm):
    l_title = StringField('Title', [validators.InputRequired()])
    description = TextAreaField('Description', [validators.InputRequired()])
    picture_path = TextAreaField('Image', [validators.InputRequired()])
    instructions_url = URLField('Instructions link', [validators.Optional()])
    submit = SubmitField("Add")

class editForm(FlaskForm):
    pass
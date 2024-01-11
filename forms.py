from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, validators, URLField, SelectField

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

class CollectionForm(FlaskForm):
    c_title = StringField('Collection Name', [validators.InputRequired()])
    submit = SubmitField("Add Collection")

class LegoCollectionForm(FlaskForm):
    dropdown = SelectField('Choose Collection: ')
    submit = SubmitField("Add to Collection")
    
    def update_choices(self, collections):
        self.dropdown.choices = []
        for collection in collections:
            new_tuple = (collection.c_id, collection.c_title)
            self.dropdown.choices.append(new_tuple)
        
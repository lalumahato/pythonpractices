from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class ContactForm(FlaskForm):
  name = StringField('Name', 
                        validators=[DataRequired(message="Enter name"), 
                        Length(min=10, max=50)])
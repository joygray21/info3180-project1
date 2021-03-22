from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class newPropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    numberOfBedrooms = StringField('No. of Rooms', validators=[InputRequired()], default="3")
    numberOfBathrooms = StringField('No. of Bathrooms', validators=[InputRequired()], default="2")
    price = StringField('Price', validators=[InputRequired()], default="15,000,000")
    pType = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    photo = FileField('Photo', 
                    validators = [
                            FileRequired(),
                            FileAllowed(['jpg', 'png', 'Images only!'])
                    ]
            )

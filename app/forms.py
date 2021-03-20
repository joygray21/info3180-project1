from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class newPropertyForm(FlaskForm):
    pTitle = StringField('Property Title', validators=[InputRequired()])
    pDesc = TextAreaField('Description', validators=[InputRequired()])
    noOfRooms = StringField('No. of Rooms', validators=[InputRequired()], default="3")
    noOfBathrooms = StringField('No. of Bathrooms', validators=[InputRequired()], default="2")
    price = StringField('Price', validators=[InputRequired()], default="15,000,000")
    pType = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[InputRequired()])
    pLoc = StringField('Location', validators=[InputRequired()])
    photo = FileField('Photo', 
                    validators = [
                            FileRequired(),
                            FileAllowed(['jpg', 'png', 'Images only!'])
                    ]
            )

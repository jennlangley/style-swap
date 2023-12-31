from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Length
from app.models import Review

class ReviewForm(FlaskForm):
    stars = IntegerField("stars", validators=[DataRequired()])
    review = StringField("review", validators=[DataRequired(), Length(min=10, max=300)])
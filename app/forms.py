from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.fields.html5 import TelField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import City

import re

class MessageForm(FlaskForm):
    author = StringField('Имя:', validators=[DataRequired(), Length(min=0, max=40, message="Поле должно содержать не более 40 символов")])
    phone = StringField('Телефон:', validators=[DataRequired()])
    city = SelectField('Город:', validators=[DataRequired()], coerce=int)
    body = TextAreaField('Сообщение:', validators=[DataRequired(), Length(min=0, max=256, message="Не более 250 символов.")])
    submit = SubmitField('Отправить')

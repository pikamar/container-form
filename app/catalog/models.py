# -*- coding: utf-8 -*-
from app import db
from wtforms import TextField, \
    SelectField, \
    FileField, \
    DateField, \
    BooleanField, \
    SelectMultipleField, \
    TextAreaField, \
    PasswordField
from wtforms.validators import InputRequired, Length
from wtforms.widgets import html_params, Select, HTMLString
from flask_wtf import FlaskForm
import datetime
import pytz

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    updated = db.Column(db.DateTime)
    status = db.Column(db.String(255))

    def __init__(self, status='new'):
        self.updated = datetime.datetime.now(pytz.timezone("Europe/Riga"))
        self.status = status

    def __repr__(self):
        return '<Data %d>' % self.id


class CustomRadioInput(Select):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        html = []
        for val, label, selected in field.iter_choices():
            #print("choices [%s] [%s] [%s]" % (val,label, selected))
            html.append(
                '<label class="btn btn-default %s"> <input type="radio" %s> %s </label>' \
                % (
                    'active' if selected else '',
                    html_params(
                        name=field.name, value=val, checked=selected, **kwargs
                    ),
                    label
                )
            )
        return HTMLString(' '.join(html))

class RadioButtonField(SelectField):
    widget = CustomRadioInput()

class SelectMultipleFieldNoValidate(SelectMultipleField):
    # Disable validation
    def pre_validate(self, form):
        pass

class SelectFieldNoValidate(SelectField):
    # Disable validation
    def pre_validate(self, form):
        pass

class DataForm(FlaskForm):
    species = RadioButtonField(
        'Species',
        validators=[InputRequired()],
        choices=[
            ('man', u'Vīrietis'),
            ('woman', u'Sieviete')
        ],
        default=''
    )
    name = TextField('Name', validators=[InputRequired(), Length(max=255)])
    password = PasswordField('Password', validators=[InputRequired(), Length(max=20)])
    birthdate = DateField('Birthdate')
    contact_lenses = BooleanField('Contact Lenses')
    profile_image = FileField('Profile image')
    foot_size = SelectFieldNoValidate('Foot size', choices=[])
    cloth_size = SelectFieldNoValidate('Cloth size', choices=[])
    subspeciality = SelectMultipleFieldNoValidate('Subspeciality', choices=[])
    experience = TextAreaField('Experience', validators=[Length(max=1000)])
    swimskill = SelectMultipleFieldNoValidate('Swim skill', choices=[])
    languageskill = SelectMultipleFieldNoValidate('Language skill', choices=[])
    want_participate = SelectMultipleFieldNoValidate('Want to participate', choices=[])

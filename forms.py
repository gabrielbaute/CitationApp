from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, URL

class ReferenceForm(FlaskForm):
    link = StringField('Enlace del Paper', validators=[DataRequired(), URL()])
    style = SelectField('Estilo de Cita', choices=[
        ('APA', 'APA'),
        ('Chicago', 'Chicago'),
        ('MLA', 'MLA'),
        ('Harvard', 'Harvard'),
        ('UNE-ISO 690:2024', 'UNE-ISO 690:2024'),
        ('IEEE', 'IEEE'),
        ('Vancouver', 'Vancouver')
    ], validators=[DataRequired()])

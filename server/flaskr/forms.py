from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, URL

class AnalyzeForm(FlaskForm):
    url = StringField('url', validators=[DataRequired(), URL()])
    ignore_cache = BooleanField('ignore_cache', default = False)

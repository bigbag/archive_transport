import wtforms_json
from wtforms import FloatField, Form, IntegerField, TextField
from wtforms.validators import *

wtforms_json.init()


class CardTrackForm(Form):
    blockid = TextField(validators=[InputRequired(), Length(max=128)])
    cardid = TextField(validators=[InputRequired(), Length(max=128)])
    carddata = TextField(validators=[InputRequired(), Length(max=128)])
    time = IntegerField(validators=[InputRequired()])
    lat = FloatField(validators=[InputRequired()])
    lon = FloatField(validators=[InputRequired()])

    def validate_csrf_token(self, field):
        pass


class BusTrackForm(Form):
    blockid = TextField(validators=[InputRequired(), Length(max=128)])
    time = IntegerField(validators=[InputRequired()])
    lat = FloatField(validators=[InputRequired()])
    lon = FloatField(validators=[InputRequired()])
    event = TextField(validators=[InputRequired(), Length(max=32)])

    def validate_csrf_token(self, field):
        pass


class PointForm(Form):
    address = TextField(validators=[InputRequired(), Length(max=256)])
    type = IntegerField(validators=[InputRequired()])
    code128 = TextField(validators=[InputRequired(), Length(max=128)])

    def validate_csrf_token(self, field):
        pass

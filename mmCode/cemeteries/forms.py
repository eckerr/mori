import wtforms
from wtforms.validators import DataRequired

from models import CemeteryEntry

class CemeteryEntryForm(wtforms.Form):
    name_of_cemetery = wtforms.StringField(
            'Cemetery name',
            validators=[DataRequired()])
    phone_of_cemetery = wtforms.StringField(
            'Phone')
    street_of_cemetery = wtforms.StringField(
            'Street address')
    city_of_cemetery = wtforms.StringField(
            'City')
    state_of_cemetery = wtforms.StringField(
            'State')
    zip_of_cemetery = wtforms.StringField(
            'Zip Code')

    def save_cemetery(self, cemetery_entry):
        self.populate_obj(cemetery_entry)
        return cemetery_entry

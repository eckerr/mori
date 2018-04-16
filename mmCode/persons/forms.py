import wtforms
from wtforms.validators import DataRequired

from models import PersonEntry

class PersonEntryForm(wtforms.Form):
    status = wtforms.SelectField(
            'status',
            choices=(
               (PersonEntry.STATUS_LIVING, 'Living'),
               (PersonEntry.STATUS_DECEASED, 'Deceased')),
               coerce=int)

    first_name = wtforms.StringField(
            'First name',
            validators=[DataRequired()])
    middle_name = wtforms.StringField(
            'Middle name')
    last_name = wtforms.StringField(
            'Last name',
            validators=[DataRequired()])
    suffix = wtforms.StringField(
            'suffix')
    nickname = wtforms.StringField(
            'Nickname')
    gender = wtforms.RadioField(
            'gender',
            choices=[
            (PersonEntry.GENDER_MALE, 'Male'),
            (PersonEntry.GENDER_FEMALE, 'Female')],
            coerce=int)
    day_of_birth_known = wtforms.BooleanField('day')
    month_of_birth_known = wtforms.BooleanField('month')
    year_of_birth_known = wtforms.BooleanField('year')

    date_of_birth = wtforms.StringField(
             'date of birth')

    day_of_death_known = wtforms.BooleanField('day')
    month_of_death_known = wtforms.BooleanField('month')
    year_of_death_known = wtforms.BooleanField('year')

    date_of_death = wtforms.StringField(
             'date of death')
    cemetery_id =wtforms.IntegerField(
            'Cemetery' )
    parents = wtforms.TextAreaField(
            'Parents')
    siblings = wtforms.TextAreaField(
            'Siblings')
    children = wtforms.TextAreaField(
            'Children')

    grave_location = wtforms.TextAreaField(
            'grave location')
    grave_GPS_long = wtforms.StringField(
            'lattitude')
    grave_GPS_lat = wtforms.StringField(
            'longitude')

    pic_thumb = wtforms.StringField(
            'thumbnail')
    pic_gstone = wtforms.StringField(
            'gravestone')
    pic_fav = wtforms.StringField(
            'Favorite pic')
    pic_other = wtforms.StringField(
            'Other pics')
    pic_description = wtforms.TextAreaField(
            'Description')
    pic_notes = wtforms.TextAreaField(
            'Notes')
    pic_bio = wtforms.TextAreaField(
            'bio')

    def save_person(self, person_entry):
        self.populate_obj(person_entry)
        return person_entry

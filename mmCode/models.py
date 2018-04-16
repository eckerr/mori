from app import db
from sqlalchemy import ForeignKey

class PersonEntry(db.Model):
    STATUS_LIVING = 0
    STATUS_DECEASED = 1
    GENDER_MALE = 0
    GENDER_FEMALE = 1

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60))
    middle_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    suffix = db.Column(db.String(10))
    nickname = db.Column(db.String(20))
    gender = db.Column(db.SmallInteger, default=GENDER_MALE)
    status = db.Column(db.SmallInteger, default=STATUS_DECEASED)
    day_of_birth_known = db.Column(db.String(1))
    month_of_birth_known = db.Column(db.String(1))
    year_of_birth_known = db.Column(db.String(1))
    day_of_death_known = db.Column(db.String(1))
    month_of_death_known = db.Column(db.String(1))
    year_of_death_known = db.Column(db.String(1))
    date_of_birth = db.Column(db.String(6))
    date_of_death = db.Column(db.String(6))
    # Cemetery
    #cemetery_id = db.relationship('CemeteryEntry',
    #    backref='person_entry', lazy=True, uselist=False)
    cemetery_id = db.Column(db.Integer, db.ForeignKey('cemetery_entry.id'))
    # grave location
    grave_location = db.Column(db.Text)
    grave_GPS_lat = db.Column(db.String(15))
    grave_GPS_lon = db.Column(db.String(15))

    # relatives
    parents = db.Column(db.Text)
    siblings = db.Column(db.Text)
    children = db.Column(db.Text)

    # pictures
    pic_thumb = db.Column(db.String(60))
    pic_gstone = db.Column(db.String(60))
    pic_fav = db.Column(db.String(60))
    pic_other = db.Column(db.String(60))
    pic_description = db.Column(db.Text)
    pic_notes = db.Column(db.Text)
    pic_bio = db.Column(db.Text)

class CemeteryEntry(db.Model):
    # cemetery
    id = db.Column(db.Integer, primary_key=True)
    name_of_cemetery = db.Column(db.String(100))
    phone_of_cemetery = db.Column(db.String(20))
    street_of_cemetery = db.Column(db.String(100))
    city_of_cemetery = db.Column(db.String(100))
    state_of_cemetery = db.Column(db.String(2))
    zip_of_cemetery = db.Column(db.String(10))
    #person_id = db.Column(db.Integer, db.ForeignKey('person_entry.id'),
    #                                       nullable=True)

    def __repr__ (self):
        return "<CemeteryEntry:(cemetery= '%s',\
                               street= '%s',\
                               city= '%s',\
                               state= '%s',\
                               zip= '%s')" %\
                               (self.name_of_cemetery,\
                               self.street_of_cemetery,\
                               self.city_of_cemetery,\
                               self.state_of_cemetery,\
                               self.zip_of_cemetery)

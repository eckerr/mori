from app import db

class PersonEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60))
    middle_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    suffix = db.Column(db.String(10))
    gender = db.Column(db.String(1))
    day_of_birth_known = db.Column(db.String(1))
    month_of_birth_known = db.Column(db.String(1))
    year_of_birth_known = db.Column(db.String(1))
    day_of_death_known = db.Column(db.String(1))
    month_of_death_known = db.Column(db.String(1))
    year_of_death_known = db.Column(db.String(1))
    # cemetery
    name_of_cemetery = db.Column(db.String(100))
    street_of_cemetery = db.Column(db.String(100))
    city_of_cemetery = db.Column(db.String(100))
    state_of_cemetery = db.Column(db.String(2))
    zip_of_cemetery = db.Column(db.String(10))
    # grave location
    grave_location = db.Column(db.Text)
    grave_GPS_lat = db.Column(db.Float)

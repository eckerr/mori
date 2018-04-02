from datetime import date

class PersonRec:
    """Object for holding person information
    :arg string first_name: first name of person
    :arg string middle_name: middle name or initial
    :arg string last_name: last name of person
    :arg string suffix: suffix, if any
    :arg string gender: 'M' for male, 'F' for female
    :arg string day_of_birth_known: 0 false, 1 true
    :arg string month_of_birth_known: 0 false, 1 true
    :arg string year_of_birth_known: 0 false, 1 true
    :arg string day_of_death_known: 0 false, 1 true
    :arg string month_of_death_known: 0 false, 1 true
    :arg string year_of_death_known: 0 false, 1 true
    :arg string date_of_birth: YYYYMMDD
    :arg string date_of_death: YYYYMMDD
    :arg string name_of_cemetery: where buried
    :arg string street_of_cemetery: street address
    :arg string city_of_cemetery: city where cemetery located
    :arg string state_of_cemetery: state where located
    :arg string zip_of_cemetery: zip code for cemetery
    :arg string grave_location: text description of location in cemetery
    :arg float grave_GPS_lat: gps lattitude
    :arg float grave_GPS_lon: gps longitude
    :arg string pic_thumb: filename for small picture of person
    :arg string pic_gstone: filename for gravestone picture
    :arg string pic_fav: filename for favorite picture of person, if present
    :arg string pic_other: filename for other picture of person
    :arg string notes: other notes pertaining to person
    :arg string bio: filename for bio description of person
    :arg string description: description line for person"""
    def __init__(self, ):
        self.first_name = ""
        self.middle_name = ""
        self.last_name = ""
        self.suffix = ""
        self.nickname = ""
        self.gender = "M"
        self.day_of_birth_known = '0'
        self.month_of_birth_known = '0'
        self.year_of_birth_known = '0'
        self.day_of_death_known = '0'
        self.month_of_death_known = '0'
        self.year_of_death_known = '0'
        self.date_of_birth = "00000000"
        self.date_of_death = "00000000"
        self.name_of_cemetery = ""
        self.street_of_cemetery = ""
        self.city_of_cemetery = ""
        self.state_of_cemetery = ""
        self.zip_of_cemetery = ""
        self.grave_location = ""
        self.grave_GPS_lat = 0.0
        self.grave_GPS_lon = 0.0
        self.pic_thumb = ""
        self.pic_gstone = ""
        self.pic_fav = ""
        self.pic_other = ""
        self.description = ""
        self.notes = ""
        self.bio = ""

    def get_stats(self):
        """method to calculate info stats

         1) if both birth and death dates exist and are valid, then using date of birth and date of death to calculate
            age at death, time since death, and current age they would have been, in years.
            2)"""
        if self.date_of_birth != "00000000" and self.date_of_death != "00000000":
            dob = self.str_to_date(self.date_of_birth)
            dod = self.str_to_date(self.dateOfDeath)
            age_at_death = (dod - dob).days // 365
            today_date = date.today()
            age_would_be = (today_date - dob).days // 365
            years_past = (today_date - dod).days // 365
            return dob, dod, age_at_death, age_would_be, years_past

    def str_to_ate(self, in_date_string):
        'method to convert date string to date object'
        return date(int(in_date_string[:4]), int(in_date_string[4:6]), int(in_date_string[6:8]))

    def print_stats(self):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                "Saturday", "Sunday"]

        dob, dod, age_at_death, age_would_be, years_past = self.get_stats()

        bwd = date.weekday(self.str_to_date(self.date_of_birth))
        dwd = date.weekday(self.str_to_date(self.date_of_death))
        if self.gender == 'M':
            gender_he = 'He'
            gender_his = 'His'
        else:
            gender_he = "She"
            gender_his = "Her"

        print()
        print(self.first_name + " " + self.middle_name + " " + self.last_name, "was born on", days[bwd] + ', ' +
              dob.strftime("%B, %d, %Y") + ".", gender_he, "died on", days[dwd] + ', ' +
              dod.strftime("%B, %d, %Y") + ' at the age of', str(age_at_death) + ".")
        print("It has been", yearsPast, "years since", gender_his.lower(), "death.", "If", gender_he.lower(),
              "were alive today,", gender_he.lower(), "would be", age_would_be, "years old.")

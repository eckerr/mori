from PersonRecClass import PersonRec

def myCreate(person):
     # test data for Marion Elaine Kerr
    person.first_name = "Marion"
    person.middle_name = "Elaine"
    person.last_name = "Kerr"
    person.suffix = ""
    person.gender = "F"
    person.day_of_birth_known = '1'
    person.month_of_birth_known = '1'
    person.year_of_birth_known = '1'
    person.day_of_death_known = '1'
    person.month_of_death_known = '1'
    person.year_of_death_known = '1'
    person.date_of_birth = "19310409"
    person.date_of_death = "19910603"
    person.name_of_cemetery = "St Joseph Catholic Cemetery"
    person.street_of_cemetery = "Belmont and Cumberland"
    person.city_of_cemetery = "River Grove"
    person.state_of_cemetery = "IL"
    person.zip_of_cemetery = "60171"
    person.grave_location = "Section V"
    person.grave_GPS_lat = 41.936978
    person.grave_GPS_lon = -87.848331
    person.pic_thumb = 'marion80x80.png'

    return person

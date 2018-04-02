from PersonRecClass import PersonRec

def myCreate(person):
    #person = PersonRec()
    # test data for Clarence F Kerr
    person.first_name = "Clarence"
    person.middle_name = "Francis"
    person.last_name = "Kerr"
    person.suffix = ""
    person.gender = "M"
    person.day_of_birth_known = '1'
    person.month_of_birth_known = '1'
    person.year_of_birth_known = '1'
    person.day_of_death_known = '1'
    person.month_of_death_known = '1'
    person.year_of_death_known = '1'
    person.date_of_birth = "19290828"
    person.date_of_death = "20041223"
    person.name_of_cemetery = "St Joseph Catholic Cemetery"
    person.street_of_cemetery = "Belmont and Cumberland"
    person.city_of_cemetery = "River Grove"
    person.state_of_cemetery = "IL"
    person.zip_of_cemetery = "60171"
    person.grave_location = "Section DD"
    person.grave_GPS_lat = 41.933164
    person.grave_GPS_lon = -87.837416
    person.pic_thumb= 'clarence80x80.png'
    
    return person

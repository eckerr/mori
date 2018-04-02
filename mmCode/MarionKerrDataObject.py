from PersonRecClass import PersonRec

def myCreate(person):
     # test data for Marion Elaine Kerr
    person.firstName = "Marion"
    person.middleName = "Elaine"
    person.lastName = "Kerr"
    person.suffix = ""
    person.gender = "F"
    person.day_of_birth_known = '1'
    person.month_of_birth_known = '1'
    person.year_of_birth_known = '1'
    person.day_of_death_known = '1'
    person.month_of_death_known = '1'
    person.year_of_death_known = '1'
    person.dateOfBirth = "19310409"
    person.dateOfDeath = "19910603"
    person.nameOfCemetery = "St Joseph Catholic Cemetery"
    person.streetOfCemetery = "Belmont and Cumberland"
    person.cityOfCemetery = "River Grove"
    person.stateOfCemetery = "IL"
    person.zipOfCemetery = "60171"
    person.graveLocation = "Section V"
    person.graveGPSlat = 41.936978
    person.graveGPSlon = -87.848331
    return person

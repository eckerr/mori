from PersonRecClass import PersonRec

def myCreate(person):
    #person = PersonRec()
    # test data for Clarence F Kerr
    person.firstName = "Clarence"
    person.middleName = "Francis"
    person.lastName = "Kerr"
    person.suffix = ""
    person.gender = "M"
    person.day_of_birth_known = '1'
    person.month_of_birth_known = '1'
    person.year_of_birth_known = '1'
    person.day_of_death_known = '1'
    person.month_of_death_known = '1'
    person.year_of_death_known = '1'
    person.dateOfBirth = "19290828"
    person.dateOfDeath = "20041223"
    person.nameOfCemetery = "St Joseph Catholic Cemetery"
    person.streetOfCemetery = "Belmont and Cumberland"
    person.cityOfCemetery = "River Grove"
    person.stateOfCemetery = "IL"
    person.zipOfCemetery = "60171"
    person.graveLocation = "Section DD"
    person.graveGPSlat = 41.933164
    person.graveGPSlon = -87.837416
    return person

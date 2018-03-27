from datetime import date

class PersonRec:
    """Object for holding person information
    :arg string firstName: first name of person
    :arg string middleName: middle name or initial
    :arg string lastName: last name of person
    :arg string suffix: suffix, if any
    :arg string gender: 'M' for male, 'F' for female
    :arg string day_of_birth_known: 0 false, 1 true
    :arg string month_of_birth_known: 0 false, 1 true
    :arg string year_of_birth_known: 0 false, 1 true
    :arg string day_of_death_known: 0 false, 1 true
    :arg string month_of_death_known: 0 false, 1 true
    :arg string year_of_death_known: 0 false, 1 true
    :arg string dateOfBirth: YYYYMMDD
    :arg string dateOfDeath: YYYYMMDD
    :arg string nameOfCemetery: where buried
    :arg string streetOfCemetery: street address
    :arg string cityOfCemetery: city where cemetery located
    :arg string stateOfCemetery: state where located
    :arg string zipOfCemetery: zip code for cemetery
    :arg string graceLocation: text description of location in cemetery
    :arg float graveGPSlat: gps lattitude
    :arg float graveGPSlon: gps longitude
    :arg string picThumb: filename for small picture of person
    :arg string picGstone: filename for gravestone picture
    :arg string picFav: filename for favorite picture of person, if present
    :arg string picOther: filename for other picture of person
    :arg string notes: other notes pertaining to person
    :arg string bio: filename for bio description of person
    :arg string description: description line for person"""
    def __init__(self, ):
        self.firstName = ""
        self.middleName = ""
        self.lastName = ""
        self.suffix = ""
        self.gender = "M"
        self.day_of_birth_known = '0'
        self.month_of_birth_known = '0'
        self.year_of_birth_known = '0'
        self.day_of_death_known = '0'
        self.month_of_death_known = '0'
        self.year_of_death_known = '0'
        self.dateOfBirth = "00000000"
        self.dateOfDeath = "00000000"
        self.nameOfCemetery = ""
        self.streetOfCemetery = ""
        self.cityOfCemetery = ""
        self.stateOfCemetery = ""
        self.zipOfCemetery = ""
        self.graveLocation = ""
        self.graveGPSlat = 0.0
        self.graveGPSlon = 0.0
        self.picThumb = ""
        self.picGstone = ""
        self.picFav = ""
        self.picOther = ""
        self.notes = ""
        self.bio = ""
        self.description = ""

    def getStats(self):
        """method to calculate info stats

         1) if both birth and death dates exist and are valid, then using date of birth and date of death to calculate
            age at death, time since death, and current age they would have been, in years.
            2)"""
        if self.dateOfBirth != "00000000" and self.dateOfDeath != "00000000":
            dob = self.strToDate(self.dateOfBirth)
            dod = self.strToDate(self.dateOfDeath)
            ageAtDeath = (dod - dob).days // 365
            todayDate = date.today()
            ageWouldBe = (todayDate - dob).days // 365
            yearsPast = (todayDate - dod).days // 365
            return dob, dod, ageAtDeath, ageWouldBe, yearsPast

    def strToDate(self, inDateString):
        'method to convert date string to date object'
        return date(int(inDateString[:4]), int(inDateString[4:6]), int(inDateString[6:8]))

    def print_stats(self):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                "Saturday", "Sunday"]

        dob, dod, ageAtDeath, ageWouldBe, yearsPast = self.getStats()

        bwd = date.weekday(self.strToDate(self.dateOfBirth))
        dwd = date.weekday(self.strToDate(self.dateOfDeath))
        if self.gender == 'M':
            genderHe = 'He'
            genderHis = 'His'
        else:
            genderHe = "She"
            genderHis = "Her"

        print()
        print(self.firstName + " " + self.middleName + " " + self.lastName, "was born on", days[bwd] + ', ' +
              dob.strftime("%B, %d, %Y") + ".", genderHe, "died on", days[dwd] + ', ' +
              dod.strftime("%B, %d, %Y") + ' at the age of', str(ageAtDeath) + ".")
        print("It has been", yearsPast, "years since", genderHis.lower(), "death.", "If", genderHe.lower(),
              "were alive today,", genderHe.lower(), "would be", ageWouldBe, "years old.")



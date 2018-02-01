from datetime import date, time, timedelta

class PersonRec:
    'Object for holding person information'
    def __init__(self, ):
        '''Initialize an empty object for person information
        Name
            First
            Middle
            last
            suffix
            gender 0 male, 1 female
        Date of Birth string YYYYMMDD
        Date of Death string YYYYMMDD
        Name of cemetery
            address
            city
            state
            zip
        Grave location
            Text location
            GPS
                lat
                Long
        Pictures
            Thumbnail
            Gravestone
            Favorite photos
            Other photos
        Notes
        Bio
        Description
        '''
        self.firstName = ""
        self.middleName = ""
        self.lastName = ""
        self.suffix = ""
        self.gender = "M"
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
        'method to calculate info stats'
        ''' 1) if both birth and death dates exist and are valid, then using date of birth and date of death to calculate 
            age at death, time since death, and current age they would have been, in years.
            2)'''
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




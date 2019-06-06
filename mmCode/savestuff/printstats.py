from mmCode.ClarenceKerrDataObject import myCreate
from mmCode.MarionKerrDataObject import myCreate as Mc

from mmCode.PersonRecClass import PersonRec
""" ************this function is NOT used, code refactored into PersonRec class  *****************"""

from datetime import date
def print_stats(person):
    days = ["Monday","Tuesday", "Wednesday", "Thursday", "Friday",
        "Saturday", "Sunday"]

    dob, dod, ageAtDeath, ageWouldBe, yearsPast, gender = person.getStats()
    bwd = date.weekday(dob)
    dwd = date.weekday(dod)
    if gender == 'M':
        genderHe = 'He'
        genderHis = 'His'
    else:
        genderHe = "She"
        genderHis = "Her"

    print()
    print(person.firstName + " " + person.middleName + " " + person.lastName, "was born on", days[bwd] + ', '+
          dob.strftime("%B, %d, %Y") + ".", genderHe, "died on", days[dwd] + ', ' + dod.strftime("%B, %d, %Y") +
         ' at the age of', str(ageAtDeath) + ".")
    print("It has been", yearsPast, "years since", genderHis.lower(), "death.", "If", genderHe.lower(),
        "were alive today,", genderHe.lower(), "would be", ageWouldBe, "years old.")


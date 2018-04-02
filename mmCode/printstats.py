from mmCode.ClarenceKerrDataObject import myCreate
from mmCode.MarionKerrDataObject import myCreate as Mc

from mmCode.PersonRecClass import PersonRec
from datetime import date

days = ["Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
person = PersonRec()
myMPerson = myCreate(person)
dob, dod, ageAtDeath, ageWouldBe, yearsPast = myMPerson.getStats()
bwd = date.weekday(dob)
dwd = date.weekday(dod)
print()
print(myMPerson.firstName + " " + myMPerson.middleName + " " + myMPerson.lastName, "was born on", days[bwd] + ', '
      + dob.strftime("%B, %d, %Y") + ".", "He", "died on", days[dwd] + ', ' + dod.strftime("%B, %d, %Y") + ' at the age of', str(ageAtDeath) + ".")
print("It has been", yearsPast, "years since", "his", "death.", "If", "he", "were alive today,", "he", "would be", ageWouldBe, "years old.")

fperson = PersonRec()
myFPerson = Mc(fperson)
dob, dod, ageAtDeath, ageWouldBe, yearsPast = myFPerson.getStats()
bwd = date.weekday(dob)
dwd = date.weekday(dod)
print()
print(myFPerson.firstName + " " + myFPerson.middleName + " " + myFPerson.lastName, "was born on", days[bwd] + ', '
      + dob.strftime("%B, %d, %Y") + ".", "She", "died on", days[dwd] + ', ' + dod.strftime("%B, %d, %Y") + ' at the age of', str(ageAtDeath) + ".")
print("It has been", yearsPast, "years since", "her", "death.", "If", "she", "were alive today,", "she", "would be", ageWouldBe, "years old.")


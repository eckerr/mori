import unittest
from unittest import TestCase
from datetime import date

from mmCode import PersonRecClass


class TestPersonRec(unittest.TestCase):
    def test_defaults(person):
        person = PersonRecClass.PersonRec()
        assert (person.firstName == "")
        assert (person.middleName == "")
        assert (person.lastName == "")
        assert (person.suffix == "")
        assert (person.gender == 'M' or person.gender == 'F')
        assert (person.day_of_birth_known == '0')
        assert (person.month_of_birth_known == '0')
        assert (person.year_of_birth_known == '0')
        assert (person.day_of_death_known == '0')
        assert (person.month_of_death_known == '0')
        assert (person.year_of_death_known == '0')
        assert (person.dateOfBirth == "00000000")
        assert (person.dateOfDeath == "00000000")
        assert (person.nameOfCemetery == "")
        assert (person.streetOfCemetery == "")
        assert (person.cityOfCemetery == "")
        assert (person.stateOfCemetery == "")
        assert (person.graveLocation == "")
        assert (person.graveGPSlat == 0.0)
        assert (person.graveGPSlon == 0.0)
        assert (person.picThumb == "")
        assert (person.picGstone == "")
        assert (person.picFav == "")
        assert (person.picOther == "")
        assert (person.notes == "")
        assert (person.bio == "")
        assert (person.description == "")

    def test_strToDate(self):
        person = PersonRecClass.PersonRec()
        person.dateOfBirth = "19290828"
        person.dateOfDeath = "20041223"
        tdate = person.strToDate(person.dateOfBirth)
        self.assertEqual(tdate, date(1929, 8, 28))
        etdate = person.strToDate(person.dateOfDeath)
        self.assertEqual(etdate, date(2004, 12, 23))

    def test_getStats(self):
        person = PersonRecClass.PersonRec()
        person.day_of_birth_known = '1'
        person.month_of_birth_known = '1'
        person.year_of_birth_known = '1'
        person.day_of_death_known = '1'
        person.month_of_death_known = '1'
        person.year_of_death_known = '1'
        person.dateOfBirth = "19290828"
        person.dateOfDeath = "20041223"
        dob, dod, ageAtDeath, ageWouldBe, yearsPast = person.getStats()
        self.assertEqual(person.day_of_birth_known, '1')
        self.assertEqual(person.month_of_birth_known, '1')
        self.assertEqual(person.year_of_birth_known, '1')
        self.assertEqual(person.day_of_death_known, '1')
        self.assertEqual(person.month_of_death_known, '1')
        self.assertEqual(person.year_of_death_known, '1')
        self.assertEqual(dob, date(1929, 8, 28))
        self.assertEqual(dod, date(2004, 12, 23))
        self.assertEqual(ageAtDeath, 75)
        self.assertEqual(ageWouldBe, 88)
        self.assertEqual(yearsPast, 13)
        assert(person.gender == 'M' or person.gender == 'F')


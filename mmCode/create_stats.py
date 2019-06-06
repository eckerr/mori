from datetime import date
def create_stats(person):
    days = ["Monday","Tuesday", "Wednesday", "Thursday", "Friday",
        "Saturday", "Sunday"]

    dob, dod, age_at_death, age_would_be, years_past = get_stats(person)
    bwd = date.weekday(dob)
    dwd = date.weekday(dod)
    if person.gender == 0:
        gender_he = 'He'
        gender_his = 'His'
    else:
        gender_he = "She"
        gender_his = "Her"


    birth_death = (person.first_name + " " + person.middle_name + " " + person.last_name, "was born on", days[bwd] + ', '+
          dob.strftime("%B, %d, %Y") + ".", gender_he, "died on", days[dwd] + ', ' + dod.strftime("%B, %d, %Y") +
         ' at the age of', str(age_at_death) + ".")
    time_past = ("It has been", str(years_past), "years since", gender_his.lower(), "death.", "If", gender_he.lower(),
        "were alive today,", gender_he.lower(), "would be", str(age_would_be), "years old.")
    return birth_death, time_past

def get_stats(person):
    if (person.day_of_birth_known == '1' and \
        person.month_of_birth_known == '1' and \
        person.year_of_birth_known == '1') and \
        (person.day_of_death_known == '1' and \
        person.month_of_death_known == '1' and \
        person.year_of_death_known == '1'):
    #if person.date_of_birth != "00000000" and person.date_of_death != "00000000":
        dob = str_to_date(person.date_of_birth)
        dod = str_to_date(person.date_of_death)
        age_at_death = (dod - dob).days // 365
        today_date = date.today()
        age_would_be = (today_date - dob).days // 365
        years_past = (today_date - dod).days // 365
        return dob, dod, age_at_death, age_would_be, years_past

def str_to_date(in_date_string):
        'method to convert date string to date object'
        return date(int(in_date_string[:4]), int(in_date_string[4:6]), int(in_date_string[6:8]))

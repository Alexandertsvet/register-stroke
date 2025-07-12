from dateutil.parser import parse
import hashlib
from datetime import datetime

def preprocessing_hash(name, surname, last_name, date_of_bersday):
    if isinstance(date_of_bersday, type(None)):
        date_of_bersday = datetime.now()
    if type(name)!='str':
        name = str(name)
    if type(surname)!='str':
        surname = str(surname)
    if type(last_name)!='str':
        last_name = str(last_name)
    if isinstance(date_of_bersday, str):
        date_of_bersday = parse(date_of_bersday)
    day, month, year = date_of_bersday.day , date_of_bersday.month, date_of_bersday.year
    str_result = ' '.join((name.lower(), surname.lower(), last_name.lower(), str(day), str(month), str(year)))
    result = hashlib.md5(str_result.encode('utf-8')).hexdigest()
    return result

import datetime

def print_header():
    print('--------------------')
    print('     BIRTHDAY APP')
    print('--------------------')
    print()


def get_birthday_from_user():
    print('What year were you born?')
    year = input('Year [YYYY]? ')
    month = input('Month [MM]? ')
    day = input('Day [DD]? ')


    # We need to get current date to calculate days
    birthday = datetime.date(int(year), int(month), int(day))
    return birthday


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(year=target_date.year, month=original_date.month, day=original_date.day)
    dt = this_year - target_date
    return dt.days


def print_birthday_information(days):
    if days < 0:
        print(f'You had you birthday {-days} days ago this year.')
    elif days > 0:
        print(f'Looks like your birthday is in {days} days.')
        print('I hope you\'re looking forward to it!')
    else:
        print('Happy Birthday!!!')


if __name__ == '__main__':
    print_header()
    bday = get_birthday_from_user()
    now = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, now)
    print_birthday_information(number_of_days)


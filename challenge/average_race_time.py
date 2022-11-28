# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime


def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()

    return content


def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""

    races = get_data()

    a = races.split('\n')
    b = [i for i in a if 'Rhines' in i]
    jenny = []
    for i in b:
        jenny.append(i.split()[0])
    print(jenny)
    return jenny


def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    total = datetime.datetime.strptime('1:02.3', '%M:%S.%f')
    print(total)
    a = datetime.timedelta(minutes=1, seconds=2)
    print('THis is time:', a+total)

    for i in racetimes:

        try:
            m, s = i.split(':')
            s, ss = s.split('.')
        except:
            m, s = i.split(':')
            total = datetime.timedelta(minutes=int(
                m), seconds=int(s), milliseconds=int(ss))
    print(total/len(racetimes))
    return total/len(racetimes)


if __name__ == '__main__':
    get_average()
# push this to github
# git add .
# git commit
# git push

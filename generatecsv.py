#!/usr/bin/python
from os.path import abspath, join, dirname
import random
import csv
full_path = lambda filename: abspath(join(dirname(__file__), filename))

#Code for name randomization
FILES = {
    'first:male': full_path('dist.male.first'),
    'first:female': full_path('dist.female.first'),
    'last': full_path('dist.all.last'),
}


def get_name(filename):
    selected = random.random() * 90
    with open(filename) as name_file:
        for line in name_file:
            name, _, cummulative, _ = line.split()
            if float(cummulative) > selected:
                return name


def get_first_name(gender=None):
    if gender not in ('male', 'female'):
        gender = random.choice(('male', 'female'))
    return get_name(FILES['first:%s' % gender]).capitalize()


def get_last_name():
    return get_name(FILES['last']).capitalize()


def get_full_name(gender=None):
    return u"%s %s" % (get_first_name(gender), get_last_name())

#Code for discombobulation
dd = {}
ban = {}
master = {}
writer = csv.writer(open('newcsv2.csv', 'w', newline=''))
for x in range (0, 4000):
    dis_banner = "%0.9d" % random.randint(0,999999)
    dis_name = ''
    if dis_banner in ban:
        for key, value in master.items():
            if dis_banner == value:
                dis_name = key
    else:
        dis_name = get_full_name()
        #Not necessary unless we want totally unique names (runtime increases a lot).
        #if dis_name in dd.values():
        #    dis_name = get_full_name()
        dd[dis_name] = dis_name
        ban[dis_banner] = dis_banner
    master[dis_name] = dis_banner
    writer.writerow([dis_name,dis_banner])
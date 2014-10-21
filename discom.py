#!/usr/bin/python
from os.path import abspath, join, dirname
import random


__title__ = 'names'
__version__ = '0.2'
__author__ = 'Trey Hunner'
__license__ = 'MIT'


full_path = lambda filename: abspath(join(dirname(__file__), filename))


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
    
name = input ("Input a name: ")
dis_name = get_full_name()
dd = {}
dd[name] = dis_name
print(dd[name])
while True:
  name = input ("Input a name: ")
  if name in dd:
    print (dd[name])
  else:
    dis_name = get_full_name()
    dd[name] = dis_name
    print(dd[name])
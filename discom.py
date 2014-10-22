#!/usr/bin/python
from os.path import abspath, join, dirname
import random
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

dd = {}
ban = {}
master = {}
while True:
  name = input ("Input a name: ")
  if name == "Stop":
    break
  elif name in dd:
    print ("%s: %s" % (dd[name], master[dd[name]]))
  else:
    banner = input ("Input a BannerID: ")
    if banner in ban:
      print (ban[banner])
      continue
    dis_name = get_full_name()
    if dis_name in dd.values():
      dis_name = get_full_name()
    dd[name] = dis_name
    dis_banner = "%0.9d" % random.randint(0,999999)
    if dis_banner in ban.values():
      dis_banner = "%0.9d" % random.randint(0,999999)
    ban[banner] = dis_banner
    master[dis_name] = dis_banner
    print("\nAvailable discombobulated identities:")
    for keys,values in master.items():
        print("%s: %s" % (keys,values))
    print("\n")
#!/usr/bin/python
from os.path import abspath, join, dirname
import random
import csv
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

name_input = []
banner_input = []
f = open('filename.csv', 'rU')
for line in f:
    cells = line.split(",")
    name_input.append(cells[0])
    banner_input.append(cells[1])
f.close()
dd = {}
ban = {}
master = {}
for x in range(0,len(banner_input)):
  name = name_input[x]
  dis_name = name
  dis_banner = 0
  if name in dd:
    dis_name = dd[name]
    #print ("%s: %s" % (dd[name], master[dd[name]]))
  banner = banner_input[x]
  if banner in ban:
    dis_banner = ban[banner]
    #for old_name, old_banner in master.items():
        #if dis_banner == old_banner:
            #dis_name = old_name
  else:
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
writer = csv.writer(open('newcsv.csv', 'w', newline=''))
for keys,values in master.items():
  print("%s: %s" % (keys,values))
  print("\n")
  writer.writerow([keys, values])
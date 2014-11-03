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
name_input = []
banner_input = []
bd_input = []
class_input = []
address_input = []
#change the following for different input files
input = input("Enter input csv: ")
f = open(input, 'rU')
for line in f:
    cells = line.split(",")
    name_input.append(cells[0])
    banner_input.append(cells[1])
    #add other collumns here.
    #bd_input.append(cells[2])
    #class_input.append(cells[3])
    #address_input.append(cells[4].rstrip('\n'))
f.close()
dd = {}
ban = {}
master = {}
#change the following for different output files
writer = csv.writer(open('newcsv.csv', 'w', newline=''))
for x in range (0, len(banner_input)):
    name = name_input[x]
    banner = banner_input[x]
    dis_name = name
    dis_banner = 0
    if banner in ban:
        dis_banner = ban[banner]
        for key, value in master.items():
            if dis_banner == value:
                dis_name = key
    else:
        dis_name = get_full_name()
        #Not necessary unless we really want to have totally unique names (runtime increases a lot)
        #if dis_name in dd.values():
        #    dis_name = get_full_name()
        dd[name] = dis_name
        dis_banner = "%0.9d" % random.randint(0,999999)
        if dis_banner in ban.values():
            dis_banner = "%0.9d" % random.randint(0,999999)
        ban[banner] = dis_banner
    master[dis_name] = dis_banner
    #change this for collumns
    #writer.writerow([dis_name,dis_banner,bd_input[x],class_input[x],address_input[x]])
    writer.writerow([dis_name,dis_banner])

#print("\nAvailable unique discombobulated identities:")
#for keys,values in master.items():
#  print("%s: %s" % (keys,values))
#  print("\n")
    

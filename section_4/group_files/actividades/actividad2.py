#!/usr/bin/env python3
from os import stat
import time

zfile = "./MyFauxCal.txt"
zInfo = stat(zfile)
zTime = time.localtime(zInfo.st_ctime)
print("Metadatos del archivo {}\n".format(zfile))
print("size = {}".format(zInfo.st_size))
print("Año//mes//dia={}/{}/{}\n".format(zTime.tm_year, zTime.tm_mon, zTime.tm_mday))

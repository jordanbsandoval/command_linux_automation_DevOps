#!/usr/bin/env python3
from os import stat
import time

zfile = "./nuevo.txt"
zinfo = stat(zfile)
ztime = time.localtime(zinfo.st_ctime)
print("\nprobando algunos modulos de time con algo del modulo stat. Sobre el archivo nuevo.txt")
print("-----------------------------------")
print("tm_year= {}\n".format(ztime.tm_year))
print("tm_mon= {}\n".format(ztime.tm_mon))
print("tm_mday= {}\n".format(ztime.tm_mday))
print("tm_hour= {}\n".format(ztime.tm_hour))
print("tm_min= {}\n".format(ztime.tm_min))
print("tm_sec= {}\n".format(ztime.tm_sec))
print("tm_wday= {}\n".format(ztime.tm_wday))
print("tm_yday= {}\n".format(ztime.tm_yday))

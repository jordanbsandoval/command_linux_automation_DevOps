#!/usr/bin/env python3
from os import stat
import time
zfile = "./prueba.txt"
zInfo = stat(zfile)
zTime = time.localtime(zInfo.st_ctime)
print("Probando algunos modulos en python\n:{}".format(zTime.tm_mon))
with open(zfile) as mt:
	print(*mt)

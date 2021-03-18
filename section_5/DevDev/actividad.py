#!/usr/bin/env python3
from subprocess import Popen
archivo = "./prueba.txt"
cal = ["cal", "-3", ">", archivo]
print("code: ", Popen(cal).wait())
with open(archivo) as fh:
	for i in fh:
		print(i[14:17])

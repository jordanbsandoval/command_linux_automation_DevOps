#!/usr/bin/env python3
from subprocess import Popen
archivo = "./prueba.txt"
print("code: ", Popen(["cal", "-3", ">", archivo]).wait())
with open(archivo) as fh:
	for line in fh:
		print(line[14:17])

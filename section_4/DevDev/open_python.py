#!/usr/bin/env python3
from os import popen
archivo = "prueba.txt"
with open(archivo) as prin:
	print(*prin)

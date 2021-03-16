#!/usr/bin/env python3
from os import popen
jfile = "./hola"
with open(jfile, "w") as fh:
	fh.write("hola como esta\n")
with open(jfile) as fj:
	print(*fj)

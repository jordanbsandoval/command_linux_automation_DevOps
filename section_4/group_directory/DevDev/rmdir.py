#!/usr/bin/env python3
from subprocess import Popen
print(Popen(["rm", "-Rf", "./prueba"]).wait())

#!/usr/bin/env python3
from subprocess import Popen
print(Popen(["cd ", "./prueba/"], shell=True).wait())

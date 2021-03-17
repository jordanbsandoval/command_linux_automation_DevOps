#!/usr/bin/env python3
from os import popen
from subprocess import Popen

print(*popen("pwd"))
Popen(['touch', 'prueba.txt']).wait()

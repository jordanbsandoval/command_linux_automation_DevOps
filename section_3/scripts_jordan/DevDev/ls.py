#!/usr/bin/env python3
from os import popen
print(*popen("ls -lha"))

#!/usr/bin/env python3
from subprocess import Popen
cmd = Popen(["whatis", "whatis"])
print(cmd.wait())

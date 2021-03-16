#!/usr/bin/env python3
from os import stat
zfile= "./hola"
zdes = stat(zfile)
print("usuario id: {}\n".format(zdes.st_uid))

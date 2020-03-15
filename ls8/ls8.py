#!/usr/bin/env python3
import sys
from cpu import CPU

try:
    cpu = CPU()
    program = sys.argv[1]
    cpu.load(program)
    cpu.run()
except IndexError:
    print('You need to include a program to run dumbass.')
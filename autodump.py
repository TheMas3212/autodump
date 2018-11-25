#!/usr/bin/env python2
#First is basic setup
import os
import sys
import subprocess

# the script expects the path to a movie file in the movies folder
movie = sys.argv[1]
# then it gets just the movie filename itself
moviename = os.path.split(movie)[1]
print(moviename)

# get base working directory
path_base = os.getcwd()

# calculate the path to various things
path_movie = os.path.join(path_base, movie)
auto_script = os.path.join(path_base, "scripts", "dumpscript.lua")

# generate the arguments for lsnes
full_lsnes = os.path.join(path_base, "lsnes-dumpavi")
arg_script = "--lua=" + auto_script
arg_dumper1 = "--dumper=INTERNAL-NULL"
arg_dumper2 = "--overdump-length=1"

if len(sys.argv) == 3:
    path_rom = "--rom=" + sys.argv[2]
else:
    path_rom = ""

# print the full command to run
print([full_lsnes, arg_dumper1, arg_dumper2, arg_script, path_movie, path_rom])
# run the full command
subprocess.call([full_lsnes, arg_dumper1, arg_dumper2, arg_script, path_movie, path_rom])

print("Dump Complete")

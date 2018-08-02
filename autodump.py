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

# create a filename for the script by removing lsmv from the movie filename and adding lua
lua_script = moviename[0:-5] + ".lua"

# calculate the path to various things
path_movie = os.path.join(path_base, movie) # movie file path
path_script = os.path.join(path_base, "dumps", lua_script) # path in dumps to put the lua script
auto_script = os.path.join(path_base, "scripts", "dumpscript.lua") # path to the real lua script

# generate the arguments for lsnes
arg_script = "--lua=" + path_script
full_lsnes = os.path.join(path_base, "lsnes-dumpavi")
arg_dumper1 = "--dumper=INTERNAL-NULL"
arg_dumper2 = "--overdump-length=1"

# create a link to the dump script in dumps with the lua script name
os.link(auto_script,path_script)

# print the full command to run
print([full_lsnes, arg_dumper1, arg_dumper2, arg_script, path_movie])

# run the full command
subprocess.call([full_lsnes, arg_dumper1, arg_dumper2, arg_script, path_movie])

# remove the link to the dump script in dumps
os.unlink(path_script)

print("Dump Complete")

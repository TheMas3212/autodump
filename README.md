Python Script used to automaticly dump lsnes movie files to r16m automatically

this script expects lsnes-dumpavi to be present in the same directory

```
[Base Folder]
    lsnes-dumpavi (executable)
    autodump.py (main python script)
    [dumps]
        (dump file appears here)
    [movies]
        lsnes_movie_file.lsmv
    [scripts]
        dumpscript.lua (modified version of the lsnes dump script)
```

dumpscript.lua is a modified version of the lsnes dump script from 
https://github.com/dwangoac/TASBot-Projects

the modifications in dumpscript.lua are
the stop_dump function has 
exec("quit-emulator")

added to it to make it quit the emulator after dumping finishes
the on_frame_emulated function has
```
    if movie.currentframe() == (movie.framecount() + 1) then
        stop_dump()
    end
```

added to the start of it to stop the dump after the movie finishes
and finaly at the end of the script outside of any functions so it gets called when the lua script gets loaded is
```
outfile = movie.get_last_movie()
outfile = string.gsub(outfile, '/movies/', '/dumps/', 1)
outfile = string.sub(outfile, 1, -6)
start_dump(outfile)
print(outfile)
exec("pause-emulator")
exec("set-speed turbo")
exec("clear-pause-on-end")
```

which in order of line
1. get the name of the loaded movie and process it to produce a filename for the dump file
2. start the dump by calling the start_dump function
3. print the output filename
4. call 'pause-emulator' to unpause the emulator
5. call 'set-speed turbo' to make sure turbo is on
6. call 'clear-pause-on-end' to make sure the emulator doesnt pause on the last frame of the movie

the python script expects a local path to a movie in the movies folder but it should work anywhere as long as its a local path
```BaseDir#./autodump.py movies/movie_to_dump.lsmv```

should make a r16m in dumps
```BaseDir/dumps/movie_to_dump.frame.r16m```

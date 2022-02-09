from build.compiler import create_executeable

class Config:
    sources = "main.c var.h print.c print.h"
    output = "hello"
    compiler = "gcc"
    flags = "-Wall"
    if flags == "":
        flags = "None"

create_executeable(Config.compiler, Config.sources, Config.output, Config.flags)
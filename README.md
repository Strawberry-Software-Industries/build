# build - Simple build System for C & C++
**You need a simple build system for C or C++? Try build!**

# What is build?
build is a build system for C and C++. It can be easily installed via pip: `pip install build-compiler`

#  How to install build?
As mentioned, with pip. See above

# How does the Build Compiler work?
To compile successfully with Build, you need a Makefile (Our is `make.py`)
Offical Example:
```py
from build.compiler import create_executeable

class Config:
    sources = "main.c var.h print.c print.h"
    output = "hello"
    compiler = "gcc"
    flags = "-Wall"
    if flags == "":
        flags = "None"

create_executeable(Config.compiler, Config.sources, Config.output, Config.flags)```

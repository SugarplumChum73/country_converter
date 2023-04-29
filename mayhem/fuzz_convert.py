#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from country_converter import convert

def GenerateString(fdp):
    str_len = fdp.ConsumeIntInRange(0, 100)
    return fdp.ConsumeUnicodeNoSurrogates(str_len)

def GenerateStringArray(fdp):
    arr_len = fdp.ConsumeIntInRange(0, 10)

    arr = []

    for i in range(arr_len):
        fuzz = GenerateString(fdp)
        arr.append(fuzz)
    
    return arr

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    arr = GenerateStringArray(fdp)
    convert(names=arr, to='name_short')

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
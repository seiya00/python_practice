import sys


def reverse(inputpath, outputpath):
    pass

def copy(inputpath, outputpath):
    with open(inputpath, 'r') as f:
        contents = f.read()
    with open(outputpath, 'w') as o:
        o.write(contents)

def duplicate(inputpath, n):
    with open(inputpath, '+') as f:
        contents = f.read()
    with open(inputpath, 'a') as f:
        for w in n:
            f.write(contents)

def replaceNeedle(inputpath, newstring):
    with open(inputpath, '+') as f:
        contents = f.read()
        while 'needle' in contents:
            f.write().replace('needle', newstring)


def main():
    command = sys.argv[1]
    inputpath = sys.argv[2]



#!/usr/bin/env python3

import sys


def main():
    name='';
    inputs=sys.argv
    if len(inputs)<2:
        name='Anonymous'
    else:
        for x in range(1,len(inputs)):          # the first argument is the file path
            if len(inputs[x].strip())>0:
                name+=inputs[x].strip() + ' '
        message(name)

def message(name):
    print('Hello, {}!'.format(name))

if __name__ == '__main__': main()

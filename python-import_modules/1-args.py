#!/usr/bin/env python3

import sys

def main():
    i = len(sys.argv) -1
    if i == 1 :
        situation = "argument"
    else:
        situation = "arguments"
    if i == 0:
        following = "."
    else:
        following = ":"
    print(i,situation,following,end="\n")
    for j in range(1,i+1):
        print("{}: {}".format(j,sys.argv[j]))
        
if __name__ == "__main__":
    main()
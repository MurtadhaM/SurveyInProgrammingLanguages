import os
import readline
f =  open('input.txt')
# print(f.readlines())
lines = list(f.readlines())
for i in lines:
    for n in range(len(lines) -1 ):
        for x in range(len(lines) - 2):
            if (int(i) + int(lines[x]) + int(lines[n])) == 2020:
                print(((i).strip() , (lines[x]).strip() , (lines[n]).strip()))
                exit(0)



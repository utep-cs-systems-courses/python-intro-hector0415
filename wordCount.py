import os
import sys
import re

if len(sys.argv) != 3:
    exit()
    
input_file = open(sys.argv[1],'r')
output_file = open(sys.argv[2],'w')

words = {}

while True:
    line = input_file.readline()
    if line == "":
        break
    split = re.split("[-.?!,\"';: |\n|\t]",line)
    for word in split:
        if word != "":
            if word.lower() in words.keys():
                words[word.lower()]+= 1
            else:
                words[word.lower()] = 1

for key in sorted(words):
    output_file.write("%s %s\n" % (key, words[key]))
    
input_file.close()
output_file.close()
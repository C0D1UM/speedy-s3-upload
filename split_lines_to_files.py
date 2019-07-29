import sys
from toolz import itertoolz

filenames = sys.stdin.readlines()
files_list = itertoolz.partition_all(10000, filenames)

for index, files in enumerate(files_list, start=0):
    outfilename = f"./output/{index}"
    with open(outfilename, 'w') as outfile:
        outfile.writelines(files)

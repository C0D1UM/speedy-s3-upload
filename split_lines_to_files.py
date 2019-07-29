import sys
from toolz import itertoolz

filenames = sys.stdin.readlines()
files_list = list(itertoolz.partition_all(10000, filenames))

for index, files in enumerate(files_list, start=0):
    with open(f"./output/{str(index)}", 'w') as outfile:
        outfile.writelines(files)

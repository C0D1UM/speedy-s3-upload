import sys
from toolz import itertoolz

'''
Program #1
Input: cat myfiles.txt | python split_lines_to_files.py
Output: Split into N files where each file is 10K files long. Last file will be remainder
'''

filenames = sys.stdin.readlines()
files_list = itertoolz.partition_all(10000, filenames)

for index, files in enumerate(files_list, start=0):
    outfilename = f"./output/{index}"
    with open(outfilename, 'w') as outfile:
        outfile.writelines(files)

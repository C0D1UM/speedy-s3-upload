import sys
import argparse
from toolz import itertoolz

'''
Program #1
Input: cat myfiles.txt | python split_stdin_to_files.py 1000
Output: Split into N files where each file is M files long where M is the script parameter. Last file will be remainder
'''

parser = argparse.ArgumentParser(description='Split file lines into multiple files. The input argument sets the number of ')
parser.add_argument('num_filenames_per_file', metavar='num_filenames_per_file', type=int,
                   help="Number of file names per file.")
args = parser.parse_args()

filenames = sys.stdin.readlines()
files_list = itertoolz.partition_all(args.num_filenames_per_file, filenames)

for index, files in enumerate(files_list, start=0):
    outfilename = f"./output/{index}"
    with open(outfilename, 'w') as outfile:
        outfile.writelines(files)

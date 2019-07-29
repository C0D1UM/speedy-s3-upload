import argparse

from shell import shell

'''
Program #2
Input: python rclone_upload_to_s3.py 0 1
'''

parser = argparse.ArgumentParser(description='Upload files to S3')
parser.add_argument('filename_begin', metavar='filename_begin', type=int,
                   help="A number that is the start of the range.")
parser.add_argument('filename_end', metavar='filename_end', type=int,
                   help='A number that is the end of the range.')
args = parser.parse_args()

filenames = range(args.filename_begin, args.filename_end+1)
for filename in filenames:
    shell(f"rclone copy -P --transfers=100 --files-from ./output/{filename} images_trial/ buyrects3\:buyrect-prod/media/_image_pac")
    print(f"{filename} copied.")





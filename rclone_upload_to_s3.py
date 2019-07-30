import argparse

from shell import shell

'''
Program #2
Input: python rclone_upload_to_s3.py 0 1
'''

parser = argparse.ArgumentParser(description='Upload files to S3 with rclone')
parser.add_argument('filename_begin', metavar='filename_begin', type=int,
                   help="A number that is the start of the range.")
parser.add_argument('filename_end', metavar='filename_end', type=int,
                   help='A number that is the end of the range.')
args = parser.parse_args()


"""
We use rclone to upload files to S3. Here's the explanation of each rclone parameter
--transfers==100                    # each upload to S3 will transfer 100 files in parallel for performance reason
--no-traverse                       # instructs rclone not to waste time traversing the S3 bucket. Also for performance reason
--files-from ./output/{filename}    # how do we know the files we want to copy? this --files-from parameter instructs the filenames we want to copy based on the file specified by ./output/{filename}
popup_image/                        # source directory you want to copy from. User configurable
buyrects3\:buyrect-prod/media/_image_pac    # destination S3 bucket along with folder name. Also, user configurable
"""

filenames = range(args.filename_begin, args.filename_end+1)
for filename in filenames:
    shell(f"rclone copy --transfers=100 --no-traverse --files-from ./output/{filename} popup_image/ buyrects3\:buyrect-prod/media/_image_pac")
    print(f"{filename} copied.")





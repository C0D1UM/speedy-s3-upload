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
print(list(filenames))

"""
for filename in filenames:
    shell(f"rclone copy -P --transfers=100 --files-from {filename} images_trial/ buyrects3\:buyrect-prod/media/_image_pac")
    print(f"{filename} copied.")
"""




'''
fp = open('myfiles.txt', 'r') 
filenames = fp.readlines()
fp.close()

def put_it(filename):
    shell(f"rclone copy --transfers=100 /Users/pac/Downloads/s3_upload_files/images/ buyrects3\:buyrect-prod/media/popup_image")
    print(f"{filename} copied.")

Get list of files from the text file as [list]
Then partition [list] to N subarrays so that there are 10K items (files) in each subarray
for each subarray in [list]:
    create a new tempdirectory
    copy files from subarry to tempdirectory
    shell(f"rclone copy --transfers=100 {tempdirectory} buyrects3\:buyrect-prod/media/_image_test")
'''
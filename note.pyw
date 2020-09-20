import argparse
import os

# Add your desired destination directory here
# The notes.txt will be created in this directory
# A great idea is to choose a directory which is shared or cloud synced
notes_destination = "E:\\Drawer\\Computer\\Python_Files\\cmd-notes"

parser = argparse.ArgumentParser(description='eg. note "This is the actual note"')
parser.add_argument('note', metavar='N', type=str, nargs='+', help='an integer for the accumulator')
args = parser.parse_args()

#with open(os.path.join(notes_destination, "notes.txt"), mode = 'a') as f:
with open(notes_destination+"\\notes.txt"), mode = 'a') as f:
    for i in range(len(args.note)):
        f.write(args.note[i])
        f.write('\n')
    f.write('\n')


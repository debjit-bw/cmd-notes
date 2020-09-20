import argparse
import os

config_parser = argparse.ArgumentParser(description="This parses the config file for target destination", fromfile_prefix_chars=">")
config_parser.add_argument("--target_destination", help="This is the target destination where the notes.txt file will be created")
config_args = config_parser.parse_args([">config"])

parser = argparse.ArgumentParser(description='eg. python note.py "This is the actual note"')
parser.add_argument('note', metavar='N', type=str, nargs='+', help='an integer for the accumulator')
args = parser.parse_args()

with open(os.path.join(config_args.target_destination, "notes.txt"), mode = 'a') as f:
    for i in range(len(args.note)):
        f.write(args.note[i])
        f.write('\n')
    f.write('\n')

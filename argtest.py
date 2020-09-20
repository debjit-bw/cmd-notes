import argparse
p0 = argparse.ArgumentParser(description="This is the desc", usage="This is the usage", epilog="This is epilogue")

p0.add_argument('--note', help='This is the note')
p0.add_argument('--text', help='This is the text of the note')
p0.parse_known_args(["--text", "this is text", '--note', "this is a note"])

args = p0.parse_args()

if __name__ == '__main__':
    print("text:" + args.text)
    print("note:" + args.note)
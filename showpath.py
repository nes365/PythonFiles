import sys
import os.path
import argparse


parser = argparse.ArgumentParser(description="Show file details")
#parser.add_argument("-h","--help", help='run "python showpath.py filename" to show details about the file.')

parser.add_argument("echo", help="echo the string you use here")
args = parser.parse_args()
print(args.echo)

file = sys.argv[1]
fullpath = os.path.abspath(file)
parentdir, file = os.path.split(fullpath)

print('FILENAME\n==> ', file)

print('PARENT DIRECTORY\n==> ', parentdir)

print('FULL PATH\n==> ', fullpath)

sys.exit(0)

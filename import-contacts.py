import argparse
import subprocess
from vcard_split import *

def import_contacts():
    args = parse_arguments() 

    #Files containing CR symbols, can't be sent to phone 
    to_unix(args.infile.name)

    split_vcards(args.infile)

def to_unix(file_path):
    command = 'dos2unix ' + file_path 
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Import contacts from vcard format to BlackBerry OS7 devices via USB')
    parser.add_argument('infile', type=open, help='Input file that contains VCard contacts')

    parser.add_argument('-e', '--erase', help='Delete all your contacts stored in phone', action="store_true")
    parser.add_argument('-p', '--password', help='Phone password. Required if phone password protection enabled', action="store_true")
    return parser.parse_args()

if __name__ == '__main__':
    import_contacts()

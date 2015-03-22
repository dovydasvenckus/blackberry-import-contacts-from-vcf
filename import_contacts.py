import argparse
import subprocess
import getpass
from vcard_split import *

def main():
    out_folder = './contacts'
    args = parse_arguments() 

    #Files containing CR symbols, can't be sent to phone 
    to_unix(args.infile.name)

    vcard_files = split_vcards(args.infile, 1, out_folder)
    
    password = parse_password(args.password)

    if (args.erase):
        delete_contacts(password, vcard_files)

    import_contacts(vcard_files, password)



def to_unix(file_path):
    command = 'dos2unix ' + file_path 
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Import contacts from vcard format to BlackBerry OS7 devices via USB')
    parser.add_argument('infile', type=open, help='Input file that contains VCard contacts')

    parser.add_argument('-e', '--erase', help='Delete all your contacts stored in phone', action="store_true")
    parser.add_argument('-p', '--password', help='Phone password. Required if phone password protection enabled', action="store_true")
    return parser.parse_args()

def parse_password(with_password):
    if with_password:
        return ' -P %s ' %getpass.getpass()
    else:
        return ''

def delete_contacts(password, vcard_files):
    #Work arround to delete contacts. Address book has only one contact that imported from vcard file
    command = 'bio -i mime -f %s -o device %s -w erase' % (vcard_files.pop(0), password)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    process.wait()

def import_contacts(vcard_files, password):
    commands = ''
    for vcard in vcard_files:
        command = 'bio -i mime -f %s -o device %s -w overwrite' % (vcard, password)
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        process.wait()

if __name__ == '__main__':
    main()

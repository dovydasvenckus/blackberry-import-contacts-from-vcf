# blackberry-import-contacts-from-vcf
## Description
Simple script to import contacts from VCF file format to blackberry OS7 phone over USB.
I wrote this script because I was frustrated that I couldn't easily import my google contacts to my blackberry device.

## Usage
1. Connect phone via USB cable to PC and select Sync Media
2. Run this script:
    python import_contacts.py myContacts.vcf

Additional flags:
* -p will ask for password
* -e will erase all contacts before importing data

## Dependencies
* Linux distribution
* Python2.7 or Python3.2
* barry-util package

## Bugs
* If you have password setup and try to use without password and after that use script with correct password import fails. You need reconect phone and enable sync mode and call script with correct password

## References / Thanks
* [Guide how to import contacts](http://www.mattvenn.net/2013/06/25/howto-import-vcard-contact-to-blackberry-curve-on-linux/comment-page-1/?rcommentid=23648&rerror=htmllang%3Den&rchash=d6bd258b4e11460231f96c61974e93b3#commentform)
* [VCard spliting script](https://gist.github.com/szczys/1478337)


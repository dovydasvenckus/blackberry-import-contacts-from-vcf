#split vcf files
import os

def split_vcards(input_file, vcards_per_file=1, working_dir = './contacts'):
    output_seed = 'contacts-part-'

    if not os.path.exists(working_dir):
        os.mkdir(working_dir)

    with input_file as f:
        count = 0
        output_count = 1
        results = []
        vcard_files = []
        for line in f:
            if ("BEGIN:VCARD" in line):
                count += 1
            if (count <= vcards_per_file):
                results.append(line)
            else:
                #output file with stored values
                vcard_files.append(write_vcards(results, build_vcard_file_name(working_dir, output_count)))

                #increment outputfile count
                output_count += 1

                #clear results list and append last read line
                del results[:]
                results.append(line)

                #set counter back to 1
                count = 1
                

        #write the last set of results to a file
        vcard_files.append(write_vcards(results, build_vcard_file_name(working_dir, output_count)))

        return vcard_files 


def build_vcard_file_name(dir_path, number, file_naming='contacts-part-', ):
    return dir_path + os.path.sep + file_naming + str(number) + '.vcf'

def write_vcards(vcards, file_path):
    with open(file_path,'w') as oFile:
        for item in vcards:
            oFile.write(item)
    return file_path


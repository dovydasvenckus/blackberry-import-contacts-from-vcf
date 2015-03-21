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
        for line in f:
            if ("BEGIN:VCARD" in line):
                count += 1
            if (count <= vcards_per_file):
                results.append(line)
            else:
                #output file with stored values
                write_vcards(results, working_dir + os.path.sep + output_seed + str(output_count))

                #increment outputfile count
                output_count += 1

                #clear results list and append last read line
                del results[:]
                results.append(line)

                #set counter back to 1
                count = 1
                

        #write the last set of results to a file
        write_vcards(results, working_dir + os.path.sep + output_seed + str(output_count))

        return working_dir + os.path.sep + output_seed + str(1) + '.vcf'

def write_vcards(vcards, file_path):
    with open(file_path + '.vcf','w') as oFile:
        for item in vcards:
            oFile.write(item)


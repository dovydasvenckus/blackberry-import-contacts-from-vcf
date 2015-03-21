#split vcf files
import os

def split_vcards(vcards_per_file=1, working_dir = './contacts', output_seed = 'contacts-part-', input_file = 'all.vcf'):

    with open(working_dir + os.path.sep + input_file,'r') as f:
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
                with open(working_dir + output_seed + str(output_count) + '.vcf','w') as oFile:
                    for item in results:
                        oFile.write(item)

                #increment outputfile count
                output_count += 1

                #clear results list and append last read line
                del results[:]
                results.append(line)

                #set counter back to 1
                count = 1
                

        #write the last set of results to a file
        with open(working_dir + output_seed + str(output_count) + '.vcf','w') as oFile:
            for item in results:
                oFile.write(item)


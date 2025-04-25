#MY FILES
'''
input_file = 'c:/Users/deeks/Downloads/python_script_files/efl1_output_filtered1000_filtered50.fasta'
output_file = 'c:/Users/deeks/Downloads/python_script_files/output_whitespace_efl1.fasta'
custom_MSA(input_file, output_file)
'''
 
#get_alignments dictionary
def read_fasta(file_path_1):
    data1 = {}
    with open(file_path_1, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            header_line = lines[i].strip()
            if header_line.startswith(">"):
                # Extract the substring after ">" and before "."
                header = header_line.split("|")[1].split("|")[0]
                sequence = lines[i+1].strip()
                data1[header] = sequence
    return data1

#usage
file_path_1 = 'c:/Users/deeks/Downloads/python_script_files/efl1_output_filtered1000_filtered50.fasta'
fasta_dict1 = read_fasta(file_path_1)
#print(fasta_dict1)

#pfam dictionary
def read_fasta(file_path_2):
    data2 = {}
    with open(file_path_2, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            header_line = lines[i].strip()
            if header_line.startswith(">"):
                # Extract the substring after ">" and before "."
                header = header_line.split(">")[1].split(".")[0]
                sequence = lines[i+1].strip()
                data2[header] = sequence
    return data2

#usage
file_path_2 = 'c:/Users/deeks/Downloads/efl1_pfam_domains/efl1-domain_N_pfam.afa_filtered25.fasta'
fasta_dict2 = read_fasta(file_path_2)
#print(fasta_dict2)

def concat_msa(fasta_dict_1, fasta_dict_2):
    data3 = {}
    for header in fasta_dict1:
        if header in fasta_dict2:
            sequence1 = fasta_dict1[header]
            sequence2 = fasta_dict2[header]
            concatenated_sequence = sequence1[:17] + sequence2 + sequence1[205:]
            data3[header] = concatenated_sequence
    return data3

fasta_dict3 = concat_msa(fasta_dict1, fasta_dict2)
#print(fasta_dict3)


def write_fasta(data, output_file):
    with open(output_file, 'w') as file:
        for header, sequence in data.items():
            file.write(f">{header}\n{sequence}\n")

# Usage to write the concatenated dictionary to a file
output_file = 'c:/Users/deeks/Downloads/hybrid_msa_efl1.fasta'
write_fasta(fasta_dict3, output_file)


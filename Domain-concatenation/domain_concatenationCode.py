#create a function that accepts fasta files
def read_fasta(file_path):
    sequences = {}
    current_sequence = ""
    with open(file_path, 'r') as f:
        for line in f.readlines():
            if line.startswith('>'):
                current_sequence = line.strip()
            else:
                sequences[current_sequence] = line.strip()
    return sequences

#program asks for 2 fasta files

    # Prompt the user to input paths to two FASTA files
file_path1 = input("Enter the path to the first FASTA file: ")
file_path2 = input("Enter the path to the second FASTA file: ")
    
# Read the sequences from the first FASTA file
alignments1 = read_fasta(file_path1)
#print(alignments1)
    
# Read the sequences from the second FASTA file
alignments2 = read_fasta(file_path2)


OX_dict_1 = {}

for header, sequence in alignments1.items():
    OXplusjunk = header[header.find("OX="):]
    OXonly = OXplusjunk[:OXplusjunk.find(" ")].strip()
    sequence_list = OX_dict_1.get(OXonly,list())
    sequence_list.append(sequence)
    OX_dict_1[OXonly] = sequence_list


OX_dict_2 = {}

for header, sequence in alignments2.items():
    OXplusjunk = header[header.find("OX="):]
    OXonly = OXplusjunk[:OXplusjunk.find(" ")].strip()
    sequence_list = OX_dict_2.get(OXonly,list())
    sequence_list.append(sequence)
    OX_dict_2[OXonly] = sequence_list

#final dictionary
concat_dict = {}

#matching dictionaries
for OX, sequence_list_1 in OX_dict_1.items():
    #print(OX, sequence_list_1)
    try: 
        sequence_list_2 = OX_dict_2[OX]
    except:
        sequence_list_2 = None
    if sequence_list_2 is not None:
        concat_list = []
        for i in range(0, len(sequence_list_1)):
            for j in range(0, len(sequence_list_2)):
                concatenation = sequence_list_1[i] + sequence_list_2[j]
                concat_list.append(concatenation)
        concat_dict[OX] = concat_list

f = open("concat_sbds_allDomains.txt", "w")
for idx, OX in enumerate(concat_dict):
    concat_list = concat_dict[OX]
    number = 0
    for i in concat_list:
        number = number + 1
        print("> ", OX, number)
        print(i)
        f.write(">" + OX + "\n")
        f.write(i + "\n")

f.close()
    

     
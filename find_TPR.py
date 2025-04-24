
def read_file(file_path):
    #ask for files
    with open(file_path, 'r') as file:
        lst = file.readlines()
    #return files to their list, if \t occurs in output list, replace with white space
    result = [line.strip().split() for line in lst]
    return [str(x[0]) + " " + str(x[1]) for x in result]

#ask for native contacts
#native_contacts_file = "c:/Users/deeks/Downloads/python_script_files/monomer_efl1_allatom_8"
#native_contacts_file = "c:/Users/deeks/Downloads/native_contacts_efl1_yeast_af_8"
native_contacts_file = "c:/Users/deeks/Downloads/sbds_fresh_start/5anc/sbds_5anc_interface_contacts_allatom"


#native_contacts_file = input("Enter list of native contacts: ")
native_contacts = read_file(native_contacts_file)
print(type(native_contacts))

#ask for DI pairs
DI_pairs_file = "c:/Users/deeks/Downloads/sbds_combined_ranked_mapped_DIs.DI"

#DI_pairs_file = input("Enter list of DI pairs: ")
DI_pairs = read_file(DI_pairs_file)
print(type(DI_pairs))

top_DIs = int(input("Enter number of Top DI pairs: "))


#find matching pairs

DI_top_pairs = DI_pairs[:top_DIs]

#find matching pairs
#true_contacts = list(set(native_contacts).intersection(set(DI_top_pairs)))
true_contacts = list(set(native_contacts).intersection(set(DI_top_pairs)))

print(true_contacts)

#output the count of native contacts
print("Number of true contacts is: ", len(true_contacts))

#True positive rate (TPR)
#TPR = len(true_contacts)/len(DI_top_pairs)
TPR = len(true_contacts)/len(DI_top_pairs)
print("The True positive rate is: ", TPR)



#find one pair in native contacts, and if its not in DI list, iterate loop to go to second pair in native contacts
#if a match exists, put the matched pair in a new list
#repeat last step until all pairs are covered
#finally, count the total number of matched pairs

#find TPR
#total number of matched pairs/total number of native contacts
# print("The TPR is" "blah blah")
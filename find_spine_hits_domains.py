
import random
import statistics

def read_file(file_path):
    #ask for files
    with open(file_path, 'r') as file:
        lst = file.readlines()
    #return files to their list, if \t occurs in output list, replace with white space
    return [line.strip().replace('\t', ' ') for line in lst]


#find top DI pairs that have spine residues. 
#No need to use true contacts for this step: because we dont need to use this structure's native contacts necessarily

def find_match(DI_top_pairs):
    result_list1 = list()
    result_list2 = list()
    for i in DI_top_pairs:
        num1, num2 = i.split(' ')
        num1 = int(num1)
        num2 = int(num2)
        if 128 <= num1 <= 157 or 228 <= num1 <=249 or 762 <= num1 <= 773 or 907 <= num1 <= 927 or 966 <= num1 <= 997 or 1001 <= num1 <= 1007 or 1034 <= num1 <= 1051:
            result_list1.append((num1, num2))
        if 128 <= num2 <= 157 or 228 <= num2 <=249 or 762 <= num2 <= 773 or 907 <= num2 <= 927 or 966 <= num2<= 997 or 1001 <= num2 <= 1007 or 1034 <= num2 <= 1051:
            result_list2.append((num1, num2))
    return (result_list1, result_list2)

def process_pairs(file_path, num_pairs):
    # Read lines from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    random_indices = random.sample(range(len(lines)), num_pairs)
    DI_top_pairs = [lines[i].strip() for i in random_indices]
    
    result_list1 = []
    result_list2 = []
    
    for pair in DI_top_pairs:
        num1, num2 = pair.split(' ')
        num1 = int(num1)
        num2 = int(num2)
        
        if 128 <= num1 <= 157 or 228 <= num1 <= 249 or 762 <= num1 <= 773 or 907 <= num1 <= 927 or 966 <= num1 <= 997 or 1001 <= num1 <= 1007 or 1034 <= num1 <= 1051:
            result_list1.append((num1, num2))
        if 128 <= num2 <= 157 or 228 <= num2 <= 249 or 762 <= num2 <= 773 or 907 <= num2 <= 927 or 966 <= num2 <= 997 or 1001 <= num2 <= 1007 or 1034 <= num2 <= 1051:
            result_list2.append((num1, num2))
    
    return result_list1, result_list2

def top_hits(DI_pairs, top_DIs):
    #find matching pairs

    DI_top_pairs = DI_pairs[:top_DIs]

    result1, result2 = find_match(DI_top_pairs)
    print("Result 1 portion")
    if result1: 
        print(result1)
        print("Number of DI pairs having 1st element as spine residue is", len(result1))
        pass
    else: print("No spine residues found.")

    print("Result2 portion")
    if result2: 
        print(result2)
        print("Number of DI pairs having 2nd element as spine residue is", len(result2))
        pass
    else: print("No spine residues found.")

    print("Union Result")
    union_result = set(result1).union(set(result2))
    final_hits = sorted(list(union_result))
    print(final_hits)
    print("Total spine hits in top DI pairs is: ", len(final_hits), ",", len(final_hits)/top_DIs)

def rand_hits(file_path, num_pairs):
    result_list1, result_list2 = process_pairs(file_path, num_pairs)
    #print("Result List 1:", result_list1)
    #print("Result List 2:", result_list2)

    union_result = set(result_list1).union(set(result_list2))
    final_hits = sorted(list(union_result))
    #print(final_hits)
    #print("Total spine hits in random DI pairs is: ", len(final_hits), ",", len(final_hits)/num_pairs)
    return (len(final_hits), len(final_hits)/num_pairs)

#ask for DI pairs
DI_pairs_file = input("Enter list of DI pairs: ")
DI_pairs = read_file(DI_pairs_file)
#num_pairs = int(input("Enter number of DI pairs to address: "))
num_pairs_list = [10, 15, 20, 30, 50, 70, 80, 100, 200, 500, 800]
avg_random_hits = []

for num_pair in num_pairs_list:
    print(num_pair)
    top_hits(DI_pairs, num_pair)
    num_random_hits = []
    n_iter = 10
    for i in range(n_iter):
        num_random_hits.append(rand_hits(DI_pairs_file, num_pair))
    avg_hits = sum([x[0] for x in num_random_hits]) / n_iter
    avg_pct_hits = sum([x[1] for x in num_random_hits]) / n_iter
    avg_random_hits.append(avg_hits)
    stdev_hits = statistics.stdev([x[0] for x in num_random_hits])
    print("avg number of random hits: ", avg_hits)
    print("avg % of random hits: ", avg_pct_hits)
    print("sd of random hits is: ", stdev_hits)


'''
# Example usage

Domain N files
c:/Users/deeks/Downloads/efl1_50/efl1_filtered_50_di_pairs_edited_ranked.DI_cols1_2_domain_N_inter
c:/Users/deeks/Downloads/hybrid_efl1/hybrid_efl1_di_pairs_ranked.DI_cols1_2_domain_N_inter
c:/Users/deeks/Downloads/efl1_70/efl1_filtered_70_di_pairs_edited_ranked.DI_cols1_2_domain_N_inter
c:/Users/deeks/Downloads/efl1_pfam_domains/DI_files/efl1_domain_N_align_ranked_matched.DI_edited

Domain C files
c:/Users/deeks/Downloads/efl1_50/efl1_filtered_50_di_pairs_edited_ranked.DI_cols1_2_domain_C_inter
c:/Users/deeks/Downloads/hybrid_efl1/hybrid_efl1_di_pairs_ranked.DI_cols1_2_domain_C_inter
c:/Users/deeks/Downloads/efl1_70/efl1_filtered_70_di_pairs_edited_ranked.DI_cols1_2_domain_C_inter
c:/Users/deeks/Downloads/efl1_pfam_domains/DI_files/efl1_concat_domain_C_align_ranked_matched.DI_edited
'''
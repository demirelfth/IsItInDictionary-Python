import json

input_file_path = "test.in.json"
output_file_path = "test.out.txt"

f = open(input_file_path)
data = json.load(f)
f.close()

syn_result = "synonyms"
dif_result = "different"
is_it_syn = False
syn_val = ""
syn_val_arr = []
syn_arr = []
result_arr = []
sub_counter = 0

test_case_number = data["T"]

for test_case in range(test_case_number):
    sub_data = data["testCases"][test_case]
    dict_length = sub_data["N"]
    que_length = sub_data["Q"]
    dict_data = sub_data["dictionary"]
    que_data = sub_data["queries"]
    for counter in range(que_length):
        is_it_syn = False
        if que_data[counter][0].lower() == que_data[counter][1].lower():
            is_it_syn = True
        syn_val = que_data[counter][0].lower()
        syn_arr = []
        if not is_it_syn:
            sub_counter = 0
            while sub_counter < dict_length:
                first_val = dict_data[sub_counter][0].lower()
                second_val = dict_data[sub_counter][1].lower()
                if syn_val not in set(syn_arr):
                    syn_arr.append(syn_val)
                    sub_counter = 0
                elif  syn_val == first_val and second_val not in set(syn_val_arr) and second_val not in set(syn_arr):
                    syn_val_arr.append(second_val)
                elif syn_val == second_val and first_val not in set(syn_val_arr) and first_val not in set(syn_arr):
                    syn_val_arr.append(first_val)
                else:
                    sub_counter += 1
                
                if len(syn_val_arr) != 0 and sub_counter == dict_length:
                    syn_val = syn_val_arr[0]
                    syn_val_arr.pop(0)
                    syn_arr.append(syn_val)
                    sub_counter = 0
                    
        if not is_it_syn and que_data[counter][1].lower() in set(syn_arr):
            is_it_syn = True
    
        if is_it_syn:
            result_arr.append(syn_result)
        else:
            result_arr.append(dif_result)

f = open(output_file_path, "w")
counter = 0
while counter < len(result_arr):
    f.write(result_arr[counter] + "\n")
    counter += 1
f.close()
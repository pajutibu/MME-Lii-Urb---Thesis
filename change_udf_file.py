import os

def change_udf_file(working_directory, udf_file_name, list_of_changed_text, list_of_new_texts, new_file_name):
    if len(list_of_changed_text) == len(list_of_new_texts) and (type(list_of_new_texts) == list and type(list_of_changed_text) == list):
        try:
            udf_file_name = working_directory + "\\" + udf_file_name
            # open and read the file
            f = open(udf_file_name, "r")
            udf_code = f.read()
            f.close()
        except:
            return print("file was not found or data type is not list")
    else:
        return print("Function Error: lists DO NOT have the same amount of elements")
    
    # start the loop of changing the 
    for i in range(len(list_of_new_texts)):
        index_change = udf_code.find(list_of_changed_text[i])
        if index_change == -1:
            return print("text specified in changable list was not found in the original file")
        else:
            udf_code = udf_code.replace(list_of_changed_text[i], list_of_new_texts[i])
    
    # open and write a new file with changed parts
    f = open(working_directory + "\\" + new_file_name, "w")
    f.write(udf_code)
    f.close()
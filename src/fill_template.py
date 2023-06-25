import pandas as pd

def get_template(template_path):
    # return template.svg content;  template_size orchard signs with numbered placeholders
    try:
        with open(template_path, 'r') as template_file:
            template = template_file.read()
            template_file.close()
    except FileNotFoundError:
        print(f"File '{template_path}' not found.")
    return template

def update_template(template_content, row, index):
    # input:
    #   the template as perhaps already modified by this function
    #   the database row 
    #   the sign sequence number 0..template_size-1
    # return:
    #   the modified template
    
    index_str = str(index)

    # replace eg "PLOT_REF_11<" with "C78<" in template_content
    new_content = template_content.replace("PLOT_"+ index_str+"<", str(row[1]["PLOT_REF"]+"<"))
    
    new_content = new_content.replace("VARIETY_"+ index_str+"<", str(row[1]["VARIETY"]+"<")) 
        
    if isinstance(row[1]["ROOTSTOCKS"], str):
        new_content = new_content.replace("ROOT_"+ index_str+"<", str(row[1]["ROOTSTOCKS"]+"<"))
    else:
        new_content = new_content.replace("ROOT_"+ index_str+"<", " <")
        
    if isinstance(row[1]["Code"], str):
        new_content = new_content.replace("POLL_"+ index_str+"<", str(row[1]["Code"]+"<"))
    else:
        new_content = new_content.replace("POLL_"+ index_str+"<", " <")
        
    return new_content


def save_template(template_content, append_filename_str):
    # save the updated template with numbered filename
    output_path = "../output/orchard_" + append_filename_str + ".svg"
    try:
        with open(output_path, 'w') as output_file:
            output_file.write(template_content)
            output_file.close()
            print("Created ", output_path)
    except FileNotFoundError:
            print(f"File '{output_path}' not created.")


def main(template_path, database_path, template_size):
    # read the database xlsx with string encoding forced
    my_orchard_data_frame = pd.read_excel(database_path, dtype="string")
    
    # identify the last row by index
    orchard_last_index = my_orchard_data_frame.last_valid_index()
    
    # my_template_num range is 0..orchard_last_index
    my_template_num = 0
    
    # position on template, range 0..template_size-1
    index = 0
    
    # int to append to each completed template filename eg orchard0.svg
    append_filename = 0
        
    # loop on rows and save every 'template_size' rows and at last row
    for row in my_orchard_data_frame.iterrows():
    
        index = my_template_num % template_size
        
        if index == 0:  # new template started
            # read the template svg file with placeholders for 12 more signs
            my_template = get_template(template_path)    
            
        # update a sign in template with row data
        my_template = update_template(my_template, row, index)
        
        if (index == (template_size-1)) or (my_template_num == orchard_last_index):
            # template full or last row of data
            append_filename_str = str(append_filename)        
            save_template(my_template, append_filename_str)
            append_filename += 1 # increment filename counter
    
        my_template_num += 1


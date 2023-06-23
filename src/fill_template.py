import pandas as pd

# source template
# template_path = "../test-data/template.svg"
template_path = "../test-data/batch_example.svg"

# source database csv
database_path = "../test-data/example.csv"

def get_template(template_path):
    # read template.svg which contains the next 12 orchard signs with placeholders
    # call this when ready to create the next 12 signs
    try:
        with open(template_path, 'r') as template_file:
            template = template_file.read()
            template_file.close()
    except FileNotFoundError:
        print(f"File '{template_path}' not found.")
    return template

def update_template(template_content, row, index):
    # input:
    #   the template as perhaps modified by this function
    #   the database row 
    #   the sign sequence number 0..last
    # return:
    #   the modified template
    
    index_str = str(index)
    
    new_content = template_content.replace("PLOT_"+ index_str, str(row[1]["Plot Reference"]))
    
    new_content = new_content.replace("VARIETY_"+ index_str, str(row[1]["Variety"])) 
        
    if isinstance(row[1]["Rootstock"], str):
        new_content = new_content.replace("ROOT_"+ index_str, str(row[1]["Rootstock"]))
    else:
        new_content = new_content.replace("ROOT_"+ index_str, " ")
        
    if isinstance(row[1]["Pollination Code"], str):
        new_content = new_content.replace("POLL_"+ index_str, str(row[1]["Pollination Code"]))
    else:
        new_content = new_content.replace("POLL_"+ index_str, " ")
        
    # return the perhaps partially updated template
    return new_content


def save_template(template_content, append_filename_str):
    # save the updated template file
    output_path = "../output/orchard_" + append_filename_str + ".svg"
    try:
        with open(output_path, 'w') as output_file:
            output_file.write(template_content)
            output_file.close()
            print("Created ", output_path)
    except FileNotFoundError:
            print(f"File '{output_path}' not created.")

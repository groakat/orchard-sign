import pandas as pd

# source template
template_path = "../test-data/template.svg"

# source database csv
database_path = "../test-data/example.csv"

def get_template_content(template_path):
    # read template.svg
    try:
        with open(template_path, 'r') as template_file:
            template_content = template_file.read()   # treat this as read only content
            template_file.close()
    except FileNotFoundError:
        print(f"File '{template_path}' not found.")
    return template_content

def create_svg_files(template_content, orchard_data_frame):
    for index, row in orchard_data_frame.iterrows():
        # replace template placeholders with text from database
        new_content = template_content.replace("plot", row["Plot Reference"])     
        new_content = new_content.replace("variety", row["Variety"])    
        if isinstance(row["Weblink"], str):                                     
            new_content = new_content.replace("weblink", row["Weblink"])
        else:
            new_content = new_content.replace("weblink", " ")
        if isinstance(row["Rootstock"], str):
            new_content = new_content.replace("rootstock", row["Rootstock"])
        else:
            new_content = new_content.replace("rootstock", " ")
        if isinstance(row["Pollination Code"], str):
            new_content = new_content.replace("pollination", row["Pollination Code"])
        else:
            new_content = new_content.replace("pollination", " ")
        if isinstance(row["Notes_1"], str):
            new_content = new_content.replace("notes_1", row["Notes_1"])
        else:
            new_content = new_content.replace("notes_1", " ")
        if isinstance(row["Notes_2"], str):
            new_content = new_content.replace("notes_2", row["Notes_2"])
        else:
            new_content = new_content.replace("notes_2", " ")

        # save the created new content as an svg file
        output_path = "../output/plot" + row["Plot Reference"] + ".svg"
        try:
            with open(output_path, 'w') as output_file:
                output_file.write(new_content)
                output_file.close()
                # print("Created file for plot", row["Plot Reference"])
        except FileNotFoundError:
                print(f"File '{output_path}' not created.")
    


# # read the database csv with string encoding forced
# my_orchard_data_frame = pd.read_csv(database_path, dtype="string")

# # read the template svg
# my_template_content = get_template_content(template_path)

# # replace template placeholders with data and save as new svg files
# create_svg_files(my_template_content, my_orchard_data_frame)

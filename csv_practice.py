# Learning how to create a csvfile, append data, and edit data in the csvfile. 

import csv
import shutil
import datetime
from tempfile import NamedTemporaryFile

def creat_new_file(file_path): # Create a csvfile or overwrite the data in the csvfile.
	with open(file_path, "w+") as csvfile: # Open the csvfile with read and write.
		fieldnames = ["ID", "NAME", "EMAIL"] 
		writer = csv.DictWriter(csvfile,fieldnames = fieldnames) # Write as dictionary.
		writer.writeheader() # Write the fieldname to the csvfile.

def get_length(file_path): # Get the aumount of the data in the csvfile.
	with open(file_path) as csvfile:
		reader = csv.reader(csvfile)
		reader_list = list(reader)
		return len(reader_list)

def append_data(file_path, name, email): # Add data into csvfile.
	with open(file_path, "a") as csvfile:
		fieldnames = ["ID", "NAME", "EMAIL"]
		next_id = get_length(file_path)
		writer = csv.DictWriter(csvfile,fieldnames = fieldnames)
		writer.writerow({
				"ID" : next_id,
				"NAME" : name,
				"EMAIL" : email
			})



def edit_csv(): # Edit the data in the csvfile.
    filename = "data.csv"
    temp_file = NamedTemporaryFile(delete = False)
    with open(filename, 'r') as csvfile, open(temp_file.name+'.tmp', 'w') as tempfile:
        reader = csv.DictReader(csvfile) # Read the csvfile.
        fieldnames = ['ID', 'NAME', 'EMAIL', 'AMOUNT', 'SENT', 'DATE']
        writer = csv.DictWriter(tempfile, fieldnames = fieldnames) # Write data into the temporary csvfile.
        writer.writeheader()
        for row in reader: # Read the data in the csvfile and write these data into temporary csvfile.
            if int(row["ID"]) == 4:
                row["SENT"] = "True"
                row["DATE"] = datetime.datetime.now()
                writer.writerow(row)
            else:
                writer.writerow({
                        "ID" : row["ID"],
                        "NAME" : row["NAME"],
                        "EMAIL" : row["EMAIL"],
                        "AMOUNT" : "123.12", # New data wrote into the temporary csvfile.
                        "SENT" : "", # New data wrote into the temporary csvfile.
                        "DATE" : datetime.datetime.now(), # New data wrote into the temporary csvfile.
                    })
        tempfile.close()
        shutil.move(tempfile.name, filename) # Move the data in the temporary csvfile to the csvfile.
edit_csv()





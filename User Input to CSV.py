# Add user input to csv

import csv

# 'a' as appending mode instead of write mode
file = open("filename.csv", "a")

name = input("Name: ")
number = input("Number: ")

# write row into csv file 
# like asking python to treat this open file as a csv file
writer = csv.writer(file)
writer.writerow([name, number])
 
file.close()


# 2nd version without file.close() cuz often forget to close
# automatically close 
with open("filename.csv", "a") as file:
    name = input("Name: ")
    number = input("Number: ")

    writer = csv.writer(file)
    # code here is easy to break if the user change the column position
    writer.writerow([name, number])
 

# 3rd version with DictWriter in case of column change
# this will ensure the input is in the respective column
with open("filename.csv", "a") as file:
    name = input("Name: ")
    number = input("Number: ")

    writer = csv.DictWriter(file, fieldnames=["name", "number"])
    writer.writerow({"name": name, "number": number})

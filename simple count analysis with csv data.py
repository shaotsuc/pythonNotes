import csv

## version 1
## getting data from csv and counting items
with open("file.csv", "r") as file:
    reader = csv.DictReader(file)
    # this may get bad if the file add new items
    a, b, c = 0, 0, 0
    for row in reader:
        favorite = row["column_name"]
        if favorite == "a":
            a += 1
        elif favorite == "b":
            b += 1
        ## no else because new item may be added
        elif favorite == "c":
            c += 1

print(f"a: {a}")
print(f"b: {b}")
print(f"b: {b}")

########################################################

## version 2
with open("file.csv", "r") as file:
    reader = csv.DictReader(file)
    ## can be dict{} too
    counts = {}
    for row in reader:
        favorite = row["column_name"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

################# small different verions to print under version 2

## if wanted to sort by item (reverse is for Desc-like)
## for favorite in sorted(counts, reverse=True):         
for favorite in counts:
    print(f"{favorite}: {counts[favorite]}")


##  if wanted to sort by count numbers - ver 1
def get_value(column_name):
    return counts[column_name]

for favorite in sorted(counts, key=get_value, reverse=True):
    print(f"{favorite}: {counts[favorite]}")

##  if wanted to sort by count numbers - ver 2
##  and you only have a function that will use once, use lambda 
for favorite in sorted(counts, key=lambda column_name: counts[column_name], reverse=True):
    print(f"{favorite}: {counts[favorite]}")
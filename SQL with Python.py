from cs50 import SQL

## in this case, it's using sqlite database
db = SQL("sqlite:///name.db")

favorite = input("Favorite: ")

## this gets back a list of dictionary from table
## ? is a placeholder and it's able to plugin user input
rows = db.execute("SELECT COUNT(*) as n FROM table where column = ?", favorite)

## as the count will get back to only one row
## version 1
row = rows[0]
print(row["n"])

## version 2 - without variable
print(row[0]["n"])
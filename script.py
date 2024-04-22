from tabulate import tabulate

a=5
b=7

sum = a+b
print(sum)

# This is additional line in my script to show how to work with packages.

table = [["Sun",696000,1989100000],["Earth",6371,5973.6],["Moon",1737,73.5],["Mars",3390,641.85]]

print(tabulate(table, tablefmt="fancy_grid"))
def csWhereIsBob(names):
    
# Sudo code 
# Define a variable "Bob" and search the list
# If Bob in list, return location
# Else return -1 

    if "Bob" in names:
        return names.index("Bob")
    else:
        return -1

print(csWhereIsBob(["Jimmy", "Layla", "Bob"]))
print(csWhereIsBob(["Bob", "Layla", "Kaitlyn", "Patricia"]))
print(csWhereIsBob(["Jimmy", "Layla", "James"]))

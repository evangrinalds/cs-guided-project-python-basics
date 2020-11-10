def csWhereIsBob(names):

    if "Bob" in names:
        return names.index("Bob")
    else:
        return -1

print(csWhereIsBob(["Jimmy", "Layla", "Bob"]))
print(csWhereIsBob(["Bob", "Layla", "Kaitlyn", "Patricia"]))
print(csWhereIsBob(["Jimmy", "Layla", "James"]))












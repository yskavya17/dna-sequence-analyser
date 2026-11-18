
dna = "ATGCCGTA"

print("DNA:", dna)
print("Length:", len(dna))

print("A count:", dna.count("A"))
print("T count:", dna.count("T"))
print("G count:", dna.count("G"))
print("C count:", dna.count("C"))

gc = dna.count("G") + dna.count("C")
print("GC percentage:", gc / len(dna) * 100)
print("")
valid = True
for letter in dna:
    if letter not in "ATGC":
        valid = False
if valid:
    print("Valid DNA!")
else:
    print("Invalid DNA!")

seq = open("arquivo.txt", "r")

seq2=seq[::-1]

replace = seq2.replace("T", "X")
replace = replace.replace("C", "Y")
replace = replace.replace("A", "T")
replace = replace.replace("G", "C")
replace = replace.replace("X", "A")
replace = replace.replace("Y", "G")

print(replace)
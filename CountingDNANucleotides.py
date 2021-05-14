seq = open("arquivo.txt", "r")

countA = seq.count("A")
countC = seq.count("C")
countG = seq.count("G")
countT = seq.count("T")

print(countA, countC, countG, countT)
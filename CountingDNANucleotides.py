with open("arquivo.txt") as arquivo:
    seq = arquivo.read()
    countA = seq.count("A")
    countC = seq.count("C")
    countG = seq.count("G")
    countT = seq.count("T")
    print(countA, countC, countG, countT)
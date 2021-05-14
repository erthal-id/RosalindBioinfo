with open("arquivo.txt") as arquivo:
    DNAseq = arquivo.read()
    RNAseq = DNAseq.replace("T", "U")
    print(RNAseq)
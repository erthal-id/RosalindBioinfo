with open("rosalind_hamm.txt") as arquivo:
    all_seq = arquivo.read()
    all_seq_split = all_seq.split('\n')
    seq1 = all_seq_split[0]
    seq2 = all_seq_split[1]
    seq1 = list(seq1)
    seq2 = list(seq2)
    contMismatch = 0.0
    contMatch = 0.0
    length = len(seq1)
    for i in range(0, length):
            if seq1[i] != seq2[i]:
                contMismatch = contMismatch + 1
            else:
                contMatch = contMatch + 1
    print(contMismatch)
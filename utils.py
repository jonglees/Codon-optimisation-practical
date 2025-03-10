
def one_hot_encode(seq):
    rna_ohe= {'A': 0, 'U': 1, 'G': 2, 'C': 3}
    one_hot_encoded = []
    for nucleotide in seq:
        rep = np.zeros(4)
        rep[rna_ohe[nucleotide]] = 1
        one_hot_encoded += (list(rep))
    return one_hot_encoded

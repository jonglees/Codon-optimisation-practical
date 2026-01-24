def one_hot_encode(seq):
    rna_ohe= {'A': 0, 'U': 1, 'G': 2, 'C': 3}
    one_hot_encoded = []
    for nucleotide in seq:
        rep = np.zeros(4)
        rep[rna_ohe[nucleotide]] = 1
        one_hot_encoded += (list(rep))
    return one_hot_encoded

print(one_hot_encode('ACGU'))
print(len(one_hot_encode('ACGU')))


import seaborn as sns
dna_positions=[]
importance_scores=[]
for dna_position, importance in enumerate(model.feature_importances_):
    dna_positions.append(dna_position)
    importance_scores.append(importance)
sns.scatterplot(x=dna_positions, y=importance_scores)

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



df_test['one_hot_encoded_seqs']=[one_hot_encode(seq) for seq in df_test.Sequence]
X_test_hidden = list(df_test['one_hot_encoded_seqs'])  # Assuming you want to use the sequence as input
y_test_hidden = list(df_test['Value'])

# Make predictions on the test set
y_pred_hidden = model.predict(X_test_hidden)



# Evaluate the model (example: Pearson Correlation)
corr = pearsonr(y_test_hidden, y_pred_hidden)
print("Pearson corr:", corr)


import seaborn as sns
dna_positions=[]
importance_scores=[]
for dna_position, importance in enumerate(model.feature_importances_):
    dna_positions.append(dna_position)
    importance_scores.append(importance)
sns.scatterplot(x=dna_positions, y=importance_scores)

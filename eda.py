# Count values and percentage for a categorical column
def count_with_percentage(df, categorical_column_name):
    s = df[categorical_column_name]
    counts = s.value_counts()
    percent = s.value_counts(normalize=True)
    percent100 = percent.mul(100).round(1).astype(str) + '%'
    return pd.DataFrame({'counts': counts, 'per': percent, 'per100': percent100})

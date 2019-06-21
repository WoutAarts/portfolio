def to_other_cat(df, col, n):
    """Convert categorical variables that aren't in top n to other"""
    value_counts = df[col].value_counts()
    idx = value_counts.index
    fltr = df[col].isin(idx[:n])
    df.loc[~fltr, col] = 'other'
    return df[col]   


def find_all_between(s, first, last):
    """Find all substrings that are between two substrings""" 
    output = []
    while first in s:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        output = output + [s[start:end]]
        s = s[end:]
    return output
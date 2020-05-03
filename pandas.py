import pandas as pd

# filter df based on column value
df[df['col'] == num]
df[df['col'].str.contains(string)]

df[(df['col 1'] == num_1) & (df['col 2'] == num_2)] # add operation
df[(df['col 1'] == num_1) | (df['col 2'] == num_2)] # or operation

# negate a boolean filter
df[~(df['col'] == num)]

# sample dataframe
df.sample(n=2)
df.sample(frac=0.5)

# specify column names from multiindex
multiindex_level = -1 #e.g.
df.columns.levels[multiindex_level]

# convert Dataframe to Dictionary where key is (row index, column name)
df.stack().to_dict()

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

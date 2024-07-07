# Exercise 4

import pandas as pd
data = {
    'a': [1, 2, 3],
    'b': [4, 5, 6]
}
index = ['c', 'd', 'e']

# Create the dataframe
df = pd.DataFrame(data, index=index)
print(df)
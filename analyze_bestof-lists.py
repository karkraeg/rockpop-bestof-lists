# %%
import pandas as pd
import json

with open('bestof-lists.json') as data_file:
    data = json.load(data_file)
# %%
df = pd.json_normalize(data, record_path=['albums'], meta=['title', 'year'], meta_prefix='list-', errors='ignore')
df
# %%
df.query('pos == 1')['artist'].value_counts().nlargest(40)
# %%
df['list-year'].value_counts()
# %%
df['artist'].value_counts().nlargest(40)
# %%
df['list-title'].value_counts().nlargest(80)

# %%

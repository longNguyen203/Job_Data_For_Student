import pandas as pd
import numpy as np


data = pd.read_json('/home/longnguyen/Documents/Coding/Project/Data-Crawler/Project-Crawl-Job_IT/data/Raw_data/company.json')
df = pd.DataFrame(data=data)

df = df.loc[(df['name'].apply(lambda x: pd.notna(x)) & (df['size'].apply(lambda x: pd.notna(x))))]

df['address'] = df['address'].apply(lambda e: e.replace("\n", ""))

df['company_intro'] = df['company_intro'].apply(lambda e: " ".join(e))
df['company_intro'] = df['company_intro'].apply(lambda e: e.replace("\n", ""))
df['company_intro'] = df['company_intro'].apply(lambda e: e.replace("●", ""))
df['company_intro'] = df['company_intro'].replace("", np.NaN)

duplicated_rows = df.duplicated()
duplicated_data = df.loc[duplicated_rows, :]
# print(df['company_intro'].head(50))
# print(df.duplicated())
# print(duplicated_data)
# print(df['name'].unique())
# print(len(df['name'].unique()))


df.to_csv('/home/longnguyen/Documents/Coding/Project/Data-Crawler/Project-Crawl-Job_IT/data/processed_data/company.csv', index=False)
import pandas as pd
import numpy as np
from datetime import datetime

## Read data
data = pd.read_json('/home/longnguyen/Documents/Coding/Project/Data-Crawler/Project-Crawl-Job_IT/data/Raw_data/result.json')
df = pd.DataFrame(data=data)

def convert_to_lower(value: str) -> float:
    if pd.notna(value):
        if "-" in value:
            lst: list = value.split("-")
            return float(lst[0])
        elif "triệu" in value:
            return float(value.replace("triệu", ""))
        else:
            price: float = float(value.replace("USD", ""))
            return price
        
def convert_to_upper(value: str) -> float:
    if pd.notna(value):
        if "-" in value:
            lst: list = value.split("-")
            if "triệu" in value:
                return float(lst[1].replace("triệu", ""))
            else:
                return float(lst[1].replace("USD", ""))
        elif "triệu" in value:
            return float(value.replace("triệu", ""))
        else:
            price: float = float(value.replace("USD", ""))
            return price
        
def currency_unit(value: str) -> str:
    if pd.notna(value):
        if 'triệu' in value: return 'VND'
        else: return 'USD'

def to_datetime(value: str) -> str:
    time: str = datetime.strptime(value, "%d/%m/%Y")
    return time

def experience_and_number_of_recruits(value: str) -> int:
    number: str = ""
    for e in value.split():
        if e.isdigit():
            number += e
    return int(number) if number else 0

## Process data
df = df.loc[(df['title'].apply(lambda x: len(x) != 0)) & (df['name'] != None)]

df['title'] = df['title'].apply(lambda e: "".join(e))
df['title'] = df['title'].apply(lambda e: e.replace("\n", ""))

df['salary'] = df['salary'].apply(lambda e: e.replace(",", ""))
df['salary'] = df['salary'].replace("Thoả thuận", None)
df['salary'] = df['salary'].str.replace(" ", "")
df['salary'] = df['salary'].str.replace("Tới", "").str.replace("Trên", "")

df["address"] = df['address'].apply(lambda e: ", ".join(e))
df["address"] = df['address'].apply(lambda e: e.replace("- ", ""))
df["address"] = df['address'].apply(lambda e: e.replace("\n", ""))

df['time'] = df['time'].apply(lambda e: "".join(e))
df['time'] = df['time'].apply(lambda e: e.replace("\n", ""))
df['time'] = df['time'].apply(lambda e: e[-10:])
df['time'] = df['time'].apply(lambda e: e.replace("/", "-"))
# df['time'] = pd.to_datetime(df['time'], format="%d-%m-%Y", errors='coerce')

df["experience"] = df["experience"].apply(experience_and_number_of_recruits)

df['number_of_recruits'] = df['number_of_recruits'].apply(experience_and_number_of_recruits)

df["description"] = df["description"].apply(lambda e: " ".join(e))
df["description"] = df["description"].apply(lambda e: e.replace("\n", ""))
df["description"] = df["description"].replace("", None)

df["requirements"] = df["requirements"].apply(lambda e: " ".join(e))
df["requirements"] = df["requirements"].apply(lambda e: e.replace("\n", ""))
df["requirements"] = df["requirements"].replace("", None)

df['benefit'] = df['benefit'].apply(lambda e: " ".join(e))
df['benefit'] = df['benefit'].apply(lambda e: e.replace("- ", ""))
df['benefit'] = df['benefit'].apply(lambda e: e.replace("●", ""))
df['benefit'] = df['benefit'].apply(lambda e: e.replace("+ ", ""))
df['benefit'] = df["benefit"].apply(lambda e: e.replace("• ", ""))
df['benefit'] = df["benefit"].apply(lambda e: e.replace("\n", ""))
df["benefit"] = df["benefit"].replace("", None)

## add column
df['lower'] = df["salary"].apply(convert_to_lower)
df['upper'] = df["salary"].apply(convert_to_upper)
df['currency_unit'] = df['salary'].apply(currency_unit)

## Move column
df.insert(3, 'lower', df.pop('lower'))
df.insert(4, 'upper', df.pop('upper'))
df.insert(5, 'currency_unit', df.pop('currency_unit'))

## drop column
df = df.drop('name', axis=1)

# print(df.head(50))
# print(df.dtypes)
# print(df[['salary', 'lower', 'upper', 'currency_unit', 'time', 'rank', 'experience', 'number_of_recruits', 'working_form']].head(50))
# print(df['benefit'].head(50))
print(df[['salary', 'lower', 'upper']].head(50))
# print(df['time'].unique())
# print(df.isna().head(50))

# df.to_csv('/home/longnguyen/Documents/Coding/Project/Data-Crawler/Project-Crawl-Job_IT/data/processed_data/results.csv', index=False)
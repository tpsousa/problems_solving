
'''numbers = [10,20,30,40,50]


print(numbers[1:4])

#list compresstion

result = [n * 2 for n in numbers if n % 2 == 0]

print(result)

#map,filter e lambda

numeros = [1,2,3,4]

result = list (map(lambda x : x * 2, numbers))

result = list(filter(lambda x : x > 3, numbers))

#criar funcoes anonimas

square = lambda x : x ** 2

print(square(5))

#dicionarios

person = {

    "name" : "Thiago",
    "age"  : 21,
    "role" : "Developer"
}

person["name"]
person["city"] = "Sao luis"
person.get("age")
person.keys()
person.values()
person.items()

n = [1,2,2,3,3,3,4]

frequency = {}

for number in numbers:

    frequency[number] = frequency.get(number, 0) + 1


unique_numbers = set(numbers)

print(unique_numbers)

print(frequency)

#operacoes importantes 

a = {1,2,3}
b = {3,4,5}

a.union(b)
a.intersection(b)
a.difference(b)

print(sorted(numbers))

print(sorted(numbers,reverse=True))

names = ["thiago","ana","pedro", "joao"]

result = sorted (names, key = len)

'''

#pandas

#dataframe e tipo uma tabela de um banco de dados

import pandas as pd

data = {

    "name" : ["ana", "pedro", "Joao", "Maria"],
    "age" : [22,25,19,30],
    "salary" : [3000, 4500, 2000,6000]
}

df = pd.DataFrame(data)

df["name"]
df[["name", "salary"]]
df.iloc[0]
df.loc[0]
df.iloc[0:2]

print("\n")

print(df)

print(df[df["salary"] > 500])

print(df [

    (df["age"] > 20) &
    (df["salary"] > 5000)
])

df["salary_double"] = df["salary"] * 2

df["name_upper"] = df["name"].str.upper()

df["salary_bonus"] = df["salary"].apply(lambda salary : salary * 1.10)

data = {

    "category" : ["food", "Drink","food", "drink","food"],
    "price" : [30,10,50,20,40]
}

dataf = pd.DataFrame(data)

print(dataf.groupby("category")["price"].sum())

dataf.groupby("category")["price"].mean()
dataf.groupby("category")["price"].count()
dataf.groupby("category")["price"].max()
dataf.groupby("category")["price"].min()

#missing values

#dados reais nem sempre estao completos, o pandas possue
#ferramentas para identificar e tratar valores ausentes

users = {

    "name" : ["ana", "pedro", "joao"],
    "age" : [22,None,19]
}

fd = pd.DataFrame(users)

print(fd["age"])

print(fd["age"].fillna(0))


df.sort_values(by= "salary",ascending=False)
df.drop_duplicates()
df.drop_duplicates(subset=["name"])

print(df.head())
print(df.tail())
#print(df.shape())
#print(df.columns())
#print(df.dtypes())
print(df.describe())

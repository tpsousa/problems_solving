
import pandas as pd


'''data = [
    {"name": "Ana", "department": "IT", "salary": 5000},
    {"name": "Pedro", "department": "HR", "salary": 3000},
    {"name": "Maria", "department": "IT", "salary": 7000},
    {"name": "Joao", "department": "Finance", "salary": 4000}
]'''


def filterEmployees(data, min_salary):

   df = pd.DataFrame(data)

   #print(df[ df["salary"].apply(lambda x : x > min_salary) ])
   print(df[ df ["salary"] > min_salary])

min_salary = 3000

#print(filterEmployees(data,min_salary))

data = [
    {"name": "Ana", "department": "IT", "salary": 5000},
    {"name": "Pedro", "department": "HR", "salary": 3000},
    {"name": "Maria", "department": "IT", "salary": 7000},
    {"name": "Joao", "department": "HR", "salary": 4000},
    {"name": "Carlos", "department": "Finance", "salary": 6000}
]

def departmentAnalysis(data):

   df = pd.DataFrame(data)

   return df.groupby("department")["salary"].mean()

#print(departmentAnalysis(data))

data = [
    {"customer": "Ana", "product": "Laptop", "amount": 3000},
    {"customer": "Pedro", "product": "Mouse", "amount": 100},
    {"customer": "Ana", "product": "Keyboard", "amount": 200},
    {"customer": "Maria", "product": "Monitor", "amount": 1500},
    {"customer": "Pedro", "product": "Laptop", "amount": 2500},
    {"customer": "Maria", "product": "Mouse", "amount": 100}
]


def CustomerPurchaseSummary(data, min_total) :

  df = pd.DataFrame(data)

  totals = df.groupby("customer")["amount"].sum()

  return totals[totals >= min_total].sort_values()


min_total = 2000

#print(CustomerPurchaseSummary(data, min_total))

data = [
    {"product": "Laptop", "price": 3000, "quantity": 2},
    {"product": "Mouse", "price": 100, "quantity": 5},
    {"product": "Laptop", "price": None, "quantity": 1},
    {"product": "Keyboard", "price": 200, "quantity": 3},
    {"product": "Mouse", "price": 100, "quantity": None},
    {"product": "Monitor", "price": 1500, "quantity": 2}
]

import pandas as pd

def CleanAndAnalyze(data):
    df = pd.DataFrame(data)
    df[["price", "quantity"]] = df[["price", "quantity"]].fillna(0)
    df["revenue"] = df["price"] * df["quantity"]

    result = df.groupby("product", as_index=False)["revenue"].sum()
    result = result.rename(columns={"revenue": "total_revenue"})

    return result.sort_values("total_revenue", ascending=False).reset_index(drop=True)

print(CleanAndAnalyze(data))
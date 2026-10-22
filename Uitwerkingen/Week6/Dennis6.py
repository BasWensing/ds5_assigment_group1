# Opdracht 2
import pandas as pd
import matplotlib.pyplot as plt

# 1
df = pd.read_excel('retail.xlsx')

categories = list(df['Category'].unique())
sales_per_category = []
categories = []

# 2a
sales_per_category = (
    df.groupby('Category')['Sales']
      .sum()
      .astype(int)
)
print(sales_per_category)


plt.bar(sales_per_category.index, sales_per_category.values)
plt.xticks(rotation = 90)
plt.title('Number of sales for each category')
plt.xlabel('Category')
plt.ylabel('Number of sales')
plt.show()

# 2b
total_sales = sum(sales_per_category.values)
df['Percentage of total sales'] = df['Sales'] / total_sales * 100
print(df)

# 2c
sales_per_month = (
    df.groupby(['Sales']['Month']
      .sum()
      .astype(int)
))
print(sales_per_month)



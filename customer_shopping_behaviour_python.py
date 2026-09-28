import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('customer_shopping_behavior.csv')

# data cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

df = df.drop_duplicates()

# print(df.head())

# fill missing values with median using categorical grouping
df['review_rating'] = df.groupby('category')['review_rating'].transform(lambda x: x.fillna(x.median()))
df.rename(columns = {'purchase_amount_usd':'purchase_amount'}, inplace = True)



# create a new column age group
labels = ['young-adult','adult','middle-aged','senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)


# create a new column for purchase frequency days
frequency_mapping = {
    'daily': 1,
    'fortnightly': 14,
    'weekly': 7,
    'bi-weekly': 14,
    'monthly': 30,
    'every-3-months': 90,
    'quarterly': 90,
    'yearly': 365
}
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)

# drop column promo_code_used
df.drop(columns=['promo_code_used'], inplace=True)

# download the cleaned dataset as csv file
df.to_csv('cleaned_customer_shopping_behavior.csv', index=False)

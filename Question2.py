import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pylab as plt 
import seaborn as sns


conn = sqlite3.connect('itdaadb.db')


query = "SELECT * FROM heart_patient"
df = pd.read_sql_query(query, conn)

"""Now lets test if there are any cleaning needed in the dataframe from the database"""

print("NULL or empty values\n",df.isna().sum())
print("\nDataTypes\n",df.dtypes)
print("\nDuplicate values\n",df.loc[df.duplicated()])
df.dropna(inplace=True)
df.drop_duplicates(keep='first',inplace=True)

print("\nDataframe cleaned")

"""Data has been cleaned and should now be plotted"""

cat_Vars = ["sex", "cp", "fbs", "restecg", "exang", "slope", "ca", "thal"]
    
for var in cat_Vars:
        sns.displot(data = df, x=var, hue="target", multiple="stack")
        plt.title(f"Distribution of {var} based on the Target variable")
        plt.show()
        
        
num_Vars = ["age","trestbps","chol","thalach","oldpeak"]
    
for var in num_Vars:
        sns.kdeplot(data=df, x=var, hue="target", fill=True)
        plt.title(f"Distribution of {var} based on the Target variable")
        plt.xlabel(var)
        plt.ylabel("Density")
        plt.show()
        
count =0
for val in df['thal']:
    if val==0:
        count=count+1
        
print(count)
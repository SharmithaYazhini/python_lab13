# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uorCbrpv_HfMIZoQrb8dRI6c7CI48fIM
"""


import streamlit as st

import pandas as pd

github_url = 'https://raw.githubusercontent.com/SharmithaYazhini/python_lab13/main/cardio_train.csv'
data = pd.read_csv(github_url, sep=';')

st.title("Lab 13 Streamlit and Backblaze")

st.write("Visualizations")

print(data.head())

def get_dataset():
    X = data[["age", "gender", "height", "weight", "ap_hi", "ap_lo", "cholesterol", "gluc", "smoke", "alco", "active"]]
    y = data["cardio"]
    return X, y

a,b= get_dataset()

"""### Exercise 1

#### Question:
Is there a correlation between age and prevelance of cardio vascular disease?
"""

import matplotlib.pyplot as plt
import seaborn as sns

without_cardio = data[data["cardio"]==0]
with_cardio= data[data["cardio"]==1]

data["age"]=round(data["age"]/365,2)

fig,ax=plt.subplots(figsize=(10, 6))
sns.boxplot(x='cardio', y='age',data=data)
ax.set_title('Distribution of Ages for Individuals with and without Cardiovascular Disease')
ax.set_xlabel('Cardiovascular Disease (0: No, 1: Yes)')
ax.set_ylabel('Age')
#plt.show()

"""#### Findings:
We can notice that from 40 years of age people get affected by cardio vascular disesase. The minimum is 40 and maximum is 65 years of age.
"""

st.pyplot(fig)

st.write("Though the overall data is from 30 years, we can notice that from 40 years of age, there is a higher likelihood that people get affected by cardio vascular disesase. The minimum is 40 and maximum is 65 years of age.")

"""#### Exercise 2
I have uploaded the data in github, And presented a part of the data in the website using streamlit
"""

subset_data = data.head(10)
st.dataframe(subset_data)


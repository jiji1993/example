import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
import seaborn as sns 
st.balloons()

df = pd.read_csv('sample.csv')
tips = df.head()
st.table(tips)
st.header("Visualisation Using Seaborn")

st.subheader("Displot")
sns.displot(tips['Period'])
st.pyplot()


st.subheader("Bar Plot")
tips.plot(kind='bar')
st.pyplot()


#pairplot
st.subheader("Pairplot")
sns.pairplot(tips,hue='STATUS',palette='rainbow')
st.pyplot()




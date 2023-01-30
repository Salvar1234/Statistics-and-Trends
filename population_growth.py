from sys import displayhook
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def bar_plot(df):
    df.plot(kind="bar",x="Country Name")
    plt.title("Population growth for different countries",size=10)
    plt.xlabel("Year",size=10)
    plt.ylabel("Population growth (annual %)",size=10)
    plt.show()
    plt.close()
def pie_plot(df):
    plt.figure(figsize=(8,8))
    print("Percentage of population growth in the year 2000:")
    plt.pie(df["2000"], labels=df["Country Name"],autopct='%1.0f%%', pctdistance=0.5, labeldistance=1.05)
    plt.show()
def correlation(df):
    print("Kendall Correlation : ")
    displayhook(df.corr(method = "kendall"))

def statProperties(y):
    print("Average: ", np.mean(y))
    print("Maximum Value :", np.max(y))
    print("Minimum value :", np.min(y))
    print("Gmean : ", stats.gmean(y))
    print("Hmean : ", stats.hmean(y))
    
df = pd.read_csv("Population_growth.csv")
displayhook(df.head())
displayhook(df.T.head())
bar_plot(df)
pie_plot(df)
correlation(df)
print("Statistical properties for different countries in the year 2000")
statProperties(df["2000"])
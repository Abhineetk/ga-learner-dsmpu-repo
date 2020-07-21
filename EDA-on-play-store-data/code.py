# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, LabelEncoder




#Loading the data
data=pd.read_csv(path)

#Code starts here
#data.hist('Rating',bins=15, figsize=(8,7))
data = data[data['Rating']<=5]
#data.hist('Rating',bins=15, figsize=(8,7), color='red')
data.isnull().sum()
data = data.dropna()
data.isnull().sum()












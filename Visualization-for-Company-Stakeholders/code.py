# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

loan_status =data['Loan_Status'].value_counts()

loan_status.plot(kind='bar',figsize=(7,5))
plt.xticks(rotation=0)

data.iloc[25,1]
data.iloc[53,9]

property_and_loan=data.groupby(['Property_Area', 'Loan_Status'])
property_and_loan=property_and_loan.size().unstack() #size and unstack convert the series data in a tabular format
property_and_loan.plot(kind='bar',stacked=False)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)

education_and_loan=data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot.bar(stacked=True, figsize=(7,5))
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)

graduate= data[data['Education']== 'Graduate']
not_graduate=data[data['Education']== 'Not Graduate']
graduate['LoanAmount'].plot(kind='density',label='Graduate')
not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate')


fig ,(ax_1,ax_2,ax_3)=plt.subplots(nrows = 3 , ncols = 1)
data.plot.scatter(x='ApplicantIncome', y='LoanAmount', ax=ax_1)
data.plot.scatter(x='CoapplicantIncome', y='LoanAmount', ax=ax_2)
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
data.plot.scatter(x='TotalIncome', y='LoanAmount', ax=ax_3)

# Step 1 
#Reading the file


#Creating a new variable to store the value counts


#Plotting bar plot



# Step 2
#Plotting an unstacked bar plot




#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 3
#Plotting a stacked bar plot




#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 4 
#Subsetting the dataframe based on 'Education' column


#Subsetting the dataframe based on 'Education' column


#Plotting density plot for 'Graduate'


#Plotting density plot for 'Graduate'


#For automatic legend display


# Step 5
#Setting up the subplots


#Plotting scatter plot


#Setting the subplot axis title


#Plotting scatter plot


#Setting the subplot axis title


#Creating a new column 'TotalIncome'


#Plotting scatter plot



#Setting the subplot axis title




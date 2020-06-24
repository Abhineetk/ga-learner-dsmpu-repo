# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

#Code starts here
fico=len(df[df['fico']>700])
total=len(df)
p_a=fico/total

purpose=len(df[df['purpose']=='debt_consolation'])
p_b=purpose/total

#f1=df[df['purpose']=='debt_consolidation']

mix=len(df[(df['fico']>700) & (df['purpose']=='debt_consolidation')])
mix_1=mix/total
p_a_b=p_a/mix_1
result=(p_a_b==p_a)
result

paid=len(df[df['paid.back.loan']=='Yes'])
prob_lp=paid/total

credit=len(df[df['credit.policy']=='Yes'])
prob_cs=credit/total

#ew_df=df[df['paid.back.loan']=='Yes']
mixx=len(df[(df['paid.back.loan']=='Yes') & (df['credit.policy']=='Yes')])
mixx_1=mixx/total
prob_pd_cs=mixx_1/prob_lp
bayes=(prob_pd_cs*prob_lp)/prob_cs
bayes

df1=df[df['paid.back.loan']=='No']
plt.figure()
xx=df1.purpose.value_counts()
xx.plot(kind='bar')


inst_median=df.installment.median()
inst_mean=df.installment.mean()
df.hist(column='installment')
df.hist(column='log.annual.inc')




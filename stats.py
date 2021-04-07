import pandas as pd
df = pd.read_csv(r'C:\Users\smarc\PycharmProjects\pythonProject\sales.csv')

mean1 = df['sales'].mean()
sum1 = df['sales'].sum()
median1 = df['sales'].median()
std1 = df['sales'].std()
var1 = df['sales'].var()

print ('Mean of Sales: ' + str(mean1))
print ('Total Sum of Sales: ' + str(sum1))
print ('Median Sales: ' + str(median1))
print ('Standard Deviation of Sales: ' + str(std1))
print ('Variance of Sales: ' + str(var1))

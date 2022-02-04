import pandas as pd
# This is a sample Python script.


#we will split the train set into train and test data in future sections
data_raw = pd.read_csv('data/AH_Provisional_COVID-19_Deaths_by_Hospital_Referral_Region.csv')


#to play with our data we'll create a copy
#remember python assignment or equal passes by reference vs values, so we use the copy function: https://stackoverflow.com/questions/46327494/python-pandas-dataframe-copydeep-false-vs-copydeep-true-vs
data1 = data_raw.copy(deep = True)

#preview data

print("\n ----------Top-5- Record----------")
print(data_raw.head(5))  #https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.head.html
# print(data_raw.tail(5)) #https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.tail.html
# print(data_raw.sample(10)) #https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sample.html
print("\n -----------Information-----------")
print(data_raw.info())  #https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.info.html
print("\n -----------Data Types-----------")
print(data_raw.dtypes)
print("\n ----------Missing value-----------")
print(data_raw.isnull().sum())
print("\n ----------Null value-----------")
print(data_raw.isna().sum())
print("\n ----------Shape of Data----------")
print(data_raw.shape)

'''Versatile data analysis laptop. It only takes one line to replace - reading your data file'''
# This is a sample Python script.
import pandas as pd
#Visualization
import matplotlib.pyplot as plt
import seaborn as sns


#we will split the train set into train and test data in future sections
# data_raw = pd.read_csv('data/AH_Provisional_COVID-19_Deaths_by_Hospital_Referral_Region.csv')
data_raw = pd.read_csv('data/arrests_ usa.csv')


#to play with our data we'll create a copy
#remember python assignment or equal passes by reference vs values, so we use the copy function:
# https://stackoverflow.com/questions/46327494/python-pandas-dataframe-copydeep-false-vs-copydeep-true-vs
data1 = data_raw.copy(deep = True)

#preview data

# to play with our data we'll create a copy
# remember python assignment or equal passes by reference vs values, so we use the copy function: https://stackoverflow.com/questions/46327494/python-pandas-dataframe-copydeep-false-vs-copydeep-true-vs
data1 = data_raw.copy(deep=True)

# preview data
print("\n ----------Top-5- Record----------")
print(data_raw.head(5))  # https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.head.html
# print(data_raw.tail(5)) #https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.tail.html
# print(data_raw.sample(10)) #https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sample.html
print("\n -----------Information-----------")
print(data_raw.info())  # https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.info.html
print("\n -----------Data Types-----------")
print(data_raw.dtypes)
print("\n ----------Missing value-----------")
print(data_raw.isnull().sum())
print("\n ----------Null value-----------")
print(data_raw.isna().sum())
print("\n ----------Shape of Data----------")
print(data_raw.shape)
print("\n ----------Number of duplicates----------")
print('Number of duplicates:', len(data_raw[data_raw.duplicated()]))


# Function to calculate missing values by column# Funct
def missing_values_table(df):
    # Total missing values
    mis_val = df.isnull().sum()

    # Percentage of missing values
    mis_val_percent = 100 * df.isnull().sum() / len(df)

    # Make a table with the results
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)

    # Rename the columns
    mis_val_table_ren_columns = mis_val_table.rename(
        columns={0: 'Missing Values', 1: '% of Total Values'})

    # Sort the table by percentage of missing descending
    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:, 1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)

    # Print some summary information
    print("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"
                                                              "There are " + str(mis_val_table_ren_columns.shape[0]) +
          " columns that have missing values.")

    # Return the dataframe with missing information
    return mis_val_table_ren_columns


missing_values_data = missing_values_table(data1)
print("\n ----------Missing values----------")
print(missing_values_data.head(30))

print("\n ----------Number of types----------")
# Number of each type of column
print(data1.dtypes.value_counts())

print("\n ----------Number of uniques----------")
# Let's now look at the number of unique entries in each of the object (categorical) columns.
print(data1.select_dtypes('object').apply(pd.Series.nunique, axis=0))

print("\n ----------Describe of tables----------")
print(data_raw.describe(include='all'))

# preview data again
print(data1.corr())

#correlation map
f, ax = plt.subplots(figsize=(18, 18))
sns.heatmap(data1.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
plt.show()

data1.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8) # ; avoid having the matplotlib verbose informations

sns.set()
sns.pairplot(data1, size = 2.5)
plt.show()
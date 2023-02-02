import pandas as pd
import matplotlib.pyplot as plt


print("\n=================== TASK 1 BELOW =====================")
# 1. Read CSV file and transfer it into DataFrame

url = "http://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv"
data = pd.read_csv(url, sep=';', header=0)

print(data)


print("\n=================== TASK 2 BELOW =====================")
# 2. Transfer object Series into index column of the dataframe

index = []
for num in range(1, len(data) + 1):
    index.append(num)
# print(index)

series = pd.Series(index)

data.set_index(series, inplace=True)
print(data)


print("\n=================== TASK 3 BELOW =====================")
# 3. Change the data in the column of DataFrame according to some condition

for index, value in data['quality'].items():
    if value < 5:
        # Modify the value
        data.at[index, 'quality'] = 5

print(data['quality'])



print("\n=================== TASK 4 BELOW =====================")
# 4. Get names of the DataFrame columns and sum of lost values DF

column_names = data.columns
# print(f'Column names: {column_names}')

# Get the sum of missing values for each column
missing_values = data.isna().sum()

print(f'Missing values: {missing_values}')


print("\n=================== TASK 5 BELOW =====================")
# 5. Exchange 2 columns, use function for it. Sort column by name

def exchange_columns(df, col1, col2):
    hold = df[col1]
    df[col1] = df[col2]
    df[col2] = hold
    df = df.rename(columns={col1: col2, col2: col1})
    return df


data = exchange_columns(data, 'quality', 'alcohol')
print(data)

data = data.sort_index(axis=1)
# print(data)


print("\n=================== TASK 6 BELOW =====================")
# 6. Delete upper and lower 5% in object DataFrame

df_5 = int(len(data.index) * (5/100))
lower_5 = df_5
upper_5 = len(data.index) - df_5
upper_bound = len(data.index)

# deleting lower and upper 5% of the dataFrame respectively
data = data.drop(index=range(1, lower_5 + 1))  # delete lower 5%
data = data.drop(index=range(upper_5, upper_bound + 1)) # delete upper 5%

print(data)


print("\n=================== TASK 7 BELOW =====================")
# 7. Replay (Apply) missed values in the Column with average values.

# Compute the average value
mean_value = data['alcohol'].mean()

# Replace missing values with the average value
data['alcohol'].fillna(mean_value, inplace=True)


print("\n=================== TASK 8 BELOW =====================")
# 8. Create two data frames using the two Dicts , Merge two data frames, and append the second data
# frame as a new column to the first data frame.

# Create the first DataFrame using a dictionary
df1 = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [50, 40, 10, 20, 30]})

# Create the second DataFrame using a dictionary
df2 = pd.DataFrame({'C': [6, 7, 8, 9, 10]})

# Merge two dataFrames
merged_df = pd.concat([df1, df2], axis=1)

# Append second df as new column to first df titled "D"
df1 = df1.assign(D=df2['C'])

# print(df1)
#
print(merged_df)


print("\n=================== TASK 9 BELOW =====================")
# 9. For any column create histogram
print("Histogram for the alcohol column in .csv file")
plt.hist(data["alcohol"])
plt.show()

# Create Pie chart
my_labels = ["Python", "Java", "JavaScript", "Go", "PHP"]
plt.pie(df1['B'], labels = my_labels)
plt.legend(title = "Backend Languages:")
plt.show()


# Create Bar chart
font = {'family':'serif','color':'blue','size':20}
plt.title("Backend Languages", fontdict = font)
plt.bar(my_labels, df1['B'], color = "#4CAf50")
plt.xlabel("Programming Language")
plt.ylabel("Number of users per 100 developers")
plt.show()


print("\n=================== TASK 10 BELOW =====================")
# 10. Create Correlation Matrix for any column

# correlation matrix containing the correlation values between column "A" and "B"
correlation_matrix = df1[["A", "B"]].corr()

print(correlation_matrix["A"])

import kagglehub #pip install kagglehub
import pandas as pd # pip install pandas

# Download latest version
path = kagglehub.dataset_download("unsdsn/world-happiness")
print("path: " + path)

years = [2015, 2016, 2017, 2018, 2019]

# All 5 dataframes for the different years will appear here
dfs: list[pd.DataFrame] = []

# Going through where the csvs were downloaded to turn them into dataframes
for year in years:
    dfs.append(pd.read_csv(path + '/' + str(year) + '.csv'))
    
# Showing you data for each of the new dataframes, some of the column names and number of columns are different
for df in dfs:
    print(df.dtypes)
    print("Number of columns: " + str(len(df.columns)))
    print("----------------------------------------")


# Continue work to clean up the dataframes, maybe make all of the dataframe into one and 
# make sure all of the column names are the same, maybe make sure all the datatypes are correct
# you could also add a 'year', maybe you don't have to merge them at all, but I think it would make it easier
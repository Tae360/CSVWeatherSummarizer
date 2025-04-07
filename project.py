import urllib.request
# Download the data
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTk6Oy_88b3OD54m5pLPsK-ZnuqLPq_Hj34N-gW04f4lks_NimigshwG_pjHV5uHIva8ansUv3c9fSG/pub?output=csv"
Filename="data-Data.csv"
urllib.request.urlretrieve(url,Filename)

import pandas as pd
# Filter the attached/linked file and keep the following columns only: STATION, NAME/LOCATION, DATE, AWND, SNOW. Then save
columns = "STATION,NAME,DATE,AWND,SNOW".strip().split(",")
# read the data
df = pd.read_csv("data-Data.csv")[columns]
# store the dataset
df.to_csv("filteredData.csv")
df.head()

# For each NAME/LOCATION, calculate the average snow amount per month. Save the results in two separate .csv files (one for
# Get the year
df['YEAR'] = df.DATE.str[-4:]
# Group by year and name and ge the mean
data = df.groupby(["YEAR","NAME"])['SNOW'].mean().reset_index()
# Store the data by year
data[data["YEAR"]=="2016"].fillna(0).drop("YEAR",axis=1).to_csv("average2016.csv")
data[data["YEAR"]=="2017"].fillna(0).drop("YEAR",axis=1).to_csv("average2017.csv")

# For each NAME/LOCATION, calculate the total/ sum snow amount per month. Save the results in two separate .csv files (one
# Repeat the above with sum instead of sum instead of mean
df['YEAR'] = df.DATE.str[-4:]
data = df.groupby(["YEAR","NAME"])['SNOW'].sum().reset_index()
data[data["YEAR"]=="2016"].fillna(0).drop("YEAR",axis=1).to_csv("total2016.csv")
data[data["YEAR"]=="2017"].fillna(0).drop("YEAR",axis=1).to_csv("total2017.csv")

# Sort the data in the files average2016.csv and average2017.csv. Store only the top 3 locations from each file. The top 3
# Sort the data and get the top 3 values using pandas mehtods
top3_2016 = pd.read_csv("total2016.csv").sort_values(by="SNOW").head(3)["NAME"].values
top3_2017 = pd.read_csv("total2017.csv").sort_values(by="SNOW").head(3)["NAME"].values
# Store the result in dataframe and save it to csv
data = pd.DataFrame(zip(top3_2016.T,top3_2017),columns=["2016","2017"])
data.to_csv("top3.csv")
# Sort values by AWNd and store it in required csv
df.sort_values(by="AWND").head(10).to_csv("top10AWND.csv")
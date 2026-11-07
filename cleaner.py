from pathlib import Path

folder = Path(__file__).parent

import pandas as pd

data = pd.read_csv(folder / "messy_data.csv")

print(data)
print("\nNumber of rows:", len(data))
print("\nMissing values:")
print(data.isnull().sum())

print("\nDuplicate rows:")
print(data.duplicated().sum())

data = data.drop_duplicates()

print("\nAfter removing duplicates:")
print(data)

data["Age"] = data["Age"].fillna(data["Age"].median())

data["City"] = data["City"].fillna("Unknown")

print("\nAfter filling missing values:")
print(data)

dates = data["Date"].astype("string")

iso = dates.str.contains(r"^\d{4}-\d{2}-\d{2}$")

clean_dates = pd.Series(index=data.index, dtype="datetime64[ns]")

clean_dates.loc[iso] = pd.to_datetime(
    dates.loc[iso], format="%Y-%m-%d"
)

clean_dates.loc[~iso] = pd.to_datetime(
    dates.loc[~iso], format="%d/%m/%Y"
)

data["Date"] = clean_dates.dt.strftime("%Y-%m-%d")

print(data)

data.to_csv(folder / "cleaned_data.csv", index=False)

print("\nCleaned data saved successfully!")

print("\nMy project folder is:")
print(Path(__file__).parent)
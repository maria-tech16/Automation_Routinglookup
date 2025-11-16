import pandas as pd

master = pd.read_excel("C:/routing_lookup/masterfile_large.xlsx")

from_location = input("Enter FROM location: ").strip().upper()
to_location = input("Enter TO location: ").strip().upper()

result = master[
    (master["From_Location"] == from_location) &
    (master["To_Location"] == to_location)
]

if not result.empty:
    print("Routing Number:", result.iloc[0]["Routing_Number"])
else:
    print("No routing found.")

'''
Energy data Q&A Tool
=====================
Reads a CSV with [Date, Energy] and answers questions like:
- Total production between a Timeperiod
'''

# Load the data from CSV
import pandas as pd

df = pd.read_csv(r"your/path/to/data.csv")

# Datetime parsing
df["Date"] = pd.to_datetime(df["Date"])

# Data Overview
print("╭" + "─"*20 + "╮")
print("│ ★ Data Overview ★  │")
print("╰" + "─"*20 + "╯")
print("🔴 Total Rows:",len(df))
print("📅 Date range:",df["Date"].min(),"to",df["Date"].max())
print("🔴 Total production:", df["Energy"].sum(),"kWh")

# QA Agent

while True:
        print()
        print("╭" + "─"*30 + "╮")
        print("│    Agent is asking.....      │")
        print("╰" + "─"*30 + "╯")
        q = input("❔ Enter the start and end dates to calculate total energy: ")
        if (q.lower()=="quit"):
            break
        try:      
            start, end = q.split("to")
            mask = (start<=df["Date"]) & (end>=df["Date"])
            f_rows = df[mask]

            if f_rows.empty:    
                print("Empty Input")
            else:           
                print()
                print("╭" + "─"*20 + "╮")
                print("│    Agent Answer    │")
                print("╰" + "─"*20 + "╯")
                Production = f_rows["Energy"].sum()

                print("Data Range Selected:",q)
                print("Selected Period Energy: " ,Production,"kWh")

        except Exception as e:
            print("Wrong input", e)

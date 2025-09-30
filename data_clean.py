"""
Attendance Data Cleaning Script 

Demonstrates:
- Connecting to Google Sheets with gspread
- Converting raw attendance data into a tidy DataFrame
- Expanding comma-separated date fields into individual rows
- Normalizing date formats
- Writing cleaned data back into a Google Sheet

Note:
This script uses a simplified approach for clarity.
"""

import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import set_with_dataframe

# Authenticate with Google Sheets API
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "your-key.json",  # replace with your service account key file
    scope
)

client = gspread.authorize(creds)

# Load raw data from export
sheet = client.open("Your Spreadsheet Name").worksheet("Raw Data")
data = sheet.get_all_records()
df = pd.DataFrame(data)

# Transform records: expand comma-separated dates into tidy rows
records = []
for _, row in df.iterrows():
    # Present dates
    for date in row["Present Dates"].split(", "):
        records.append({
            "Student ID": row["Student ID"],
            "Date": date,
            "Status": "Present",
            "Grade": row["Grade"]
        })

    # Absent dates
    for date in row["Absent Dates"].split(", "):
        records.append({
            "Student ID": row["Student ID"],
            "Date": date,
            "Status": "Absent",
            "Grade": row["Grade"]
        })

    # Late dates
    for date in row["Late Dates"].split(", "):
        records.append({
            "Student ID": row["Student ID"],
            "Date": date,
            "Status": "Late",
            "Grade": row["Grade"]
        })

clean_df = pd.DataFrame(records)

# Normalize and format dates
clean_df["Date"] = clean_df["Date"].str.extract(r"(\d{1,2}/\d{1,2}/\d{2,4})")
clean_df["Date"] = pd.to_datetime(clean_df["Date"], errors="coerce")
clean_df["Date"] = clean_df["Date"].dt.strftime("%m/%d/%Y")

# Write cleaned data to a new worksheet
sheet_out = client.open("Your Spreadsheet Name").worksheet("Cleaned Data")
sheet_out.clear()
set_with_dataframe(sheet_out, clean_df)

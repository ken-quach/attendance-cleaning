# attendance-data-pipeline
This script automates the transformation of student attendance data from Google Sheets for visualization in Tableau. It normalizes multi-date fields into individual rows and tags attendance status ("Present", "Absent", "Late") for time-series analysis.

# Attendance Cleaning Pipeline (Demo)

## 📌 Overview
This project demonstrates a simple **ETL pipeline** built with **Python**, **Pandas**, and the **Google Sheets API**.  

The script takes raw student attendance data (where attendance dates are stored as comma-separated strings) and restructures it into a **clean, analysis-ready dataset**.  

⚠️ This is a **simplified demo version** intended for portfolio purposes. It uses placeholder sheet names and dummy data — no private credentials or real records are included.  

---

## ⚙️ Features
- Connects to Google Sheets using a service account  
- Expands comma-separated attendance dates into individual rows  
- Normalizes inconsistent date formats  
- Loads cleaned data back into a new Google Sheet  

---

## 📊 Example Input (Raw Data)
| Student ID | Grade | Present Dates     | Absent Dates | Late Dates |
|------------|-------|------------------|--------------|------------|
| 1001       | 5     | 9/1/25, 9/2/25  | 9/3/25       |            |
| 1002       | 6     | 9/1/25          |              | 9/2/25     |

---

## 📈 Example Output (Clean Data)
| Student ID | Date     | Status  | Grade |
|------------|----------|---------|-------|
| 1001       | 09/01/25 | Present | 5     |
| 1001       | 09/02/25 | Present | 5     |
| 1001       | 09/03/25 | Absent  | 5     |
| 1002       | 09/01/25 | Present | 6     |
| 1002       | 09/02/25 | Late    | 6     |

---

## 🛠️ Tech Stack
- **Python**: pandas, gspread, oauth2client  
- **Google Sheets API** for data extraction and loading  
- **ETL principles** (Extract → Transform → Load)  

---

## 🚀 How It Works
1. **Extract**: Pulls raw attendance data from Google Sheets (`Raw Data` tab).  
2. **Transform**: Splits comma-separated date fields into tidy rows and normalizes formats.  
3. **Load**: Pushes the cleaned dataset into a new Google Sheet (`Cleaned Data` tab).  





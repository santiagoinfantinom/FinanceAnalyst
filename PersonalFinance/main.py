import pandas as pd
import csv
from datetime import datetime
from data_entry import get_date,get_amount,get_category,get_description

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"
    
    @classmethod
    def intialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False) #Index False cause were not gonna sort it

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date":date,
            "amount":amount,
            "category":category,
            "description":description 

        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames= cls.COLUMNS)
            writer.writerow(new_entry)
            #Python will handle closing the file for you!

        print("Entry added successfully")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        
        # Strip time from datetime entries by converting to date-only (if time exists)
        df["date"] = pd.to_datetime(df["date"], errors='coerce').dt.date  # Coerce invalid dates to NaT and keep only the date
        
        start_date = datetime.strptime(start_date, CSV.FORMAT).date()  # Ensure start and end are date-only
        end_date = datetime.strptime(end_date, CSV.FORMAT).date()

        # Filter the data based on the start and end dates
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No results!")
        else:
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))

            total_income = filtered_df[filtered_df["category"] == "income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "expense"]["amount"].sum()
            print("\nSummary:")
            print(f"Total income: ${total_income:.2f}")
            print(f"Total expense: ${total_expense:.2f}")
            print(f"Net Savings: ${(total_income - total_expense):.2f}")

        return filtered_df

def add():
    CSV.intialize_csv() 
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ", allow_default=True)   
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category,description)


CSV.get_transactions("01-01-2023", "31-12-2025")


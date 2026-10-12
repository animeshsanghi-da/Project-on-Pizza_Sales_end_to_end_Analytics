# main.py

import pandas as pd
from utils import get_db_engine

def load_data_to_mysql(file_path: str, table_name: str = "pizza_sales"):
    try:
        print("1. Reading data file...")
        df = pd.read_excel(file_path)

        print("2. Formatting dates and times for MySQL...")
        # YYYY-MM-DD
        df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True).dt.strftime('%Y-%m-%d')

        # HH:MM:SS
        df['order_time'] = pd.to_datetime(df['order_time'], dayfirst=True).dt.strftime('%H:%M:%S')

        print("3. Connecting to MySQL database...")
        engine = get_db_engine()

        print(f"4. Uploading {len(df)} rows to table '{table_name}'...")
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace",  # Options: 'append', 'replace', or 'fail'
            index=False,
            chunksize=1000       # Uploads data in batches for high performance
        )
        
        print("Data loaded successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    FILE_PATH = "../../02_Transformed_data/pizza_sales_transformed_data.xlsx"
    load_data_to_mysql(FILE_PATH)
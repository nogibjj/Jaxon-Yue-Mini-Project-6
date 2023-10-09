import os
import pandas as pd
from databricks import sql
from dotenv import load_dotenv

def extract_wages_from_files(file_path1="dataset/Development of Average Annual Wages_1.csv",
                             file_path2="dataset/Development of Average Annual Wages_2.csv"):
    """Extract wage data from two file paths."""
    df1 = pd.read_csv(file_path1, delimiter=",", skiprows=1)
    df2 = pd.read_csv(file_path2, delimiter=",", skiprows=1)
    return df1, df2

def load_table(dataset, table_name, columns):
    df = pd.read_csv(dataset, delimiter=",", skiprows=1)
    load_dotenv()
    host = os.getenv("HOST_NAME")
    token = os.getenv("TOKEN")
    path = os.getenv("HTTP_PATH")

    with sql.connect(
        server_hostname=host,
        access_token=token,
        http_path=path,
    ) as connection:
        c = connection.cursor()
        
        c.execute(f"SHOW TABLES FROM default LIKE '{table_name}'")
        result = c.fetchall()
        if not result:
            table_columns = ", ".join(columns)
            c.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({table_columns})")

        # Insert data from the dataframe into the table
        for _, row in df.iterrows():
            convert = tuple(row)
            c.execute(f"INSERT INTO {table_name} VALUES {convert}")
        
        c.close()

    return "success"

def query():
    load_dotenv()
    host = os.getenv("HOST_NAME")
    token = os.getenv("TOKEN")
    path = os.getenv("HTTP_PATH")
    with sql.connect(
        server_hostname=host,
        access_token=token,
        http_path=path,
    ) as connection:
        c = connection.cursor()
        c.execute("""
            SELECT w1.Region, w1.Country, w1.year_2000, w1.year_2010, w1.year_2020, w2.year_2022, AVG(w2.year_2022) OVER(PARTITION BY w1.Region) as avg_year_2022
            FROM wages_1 w1
            JOIN wages_2 w2 ON w1.Country = w2.Country
            ORDER BY avg_year_2022 DESC, w1.Country
        """)
        results = c.fetchall()
        c.close()

    top_regions = set([row[0] for row in results[:3]])
    filtered_results = [row for row in results if row[0] in top_regions]
    
    return filtered_results

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

def load_table(dataset1="dataset/Development of Average Annual Wages_1.csv",
        dataset2="dataset/Development of Average Annual Wages_2.csv"):
    """"Transforms and Loads data into the Databricks database"""
    df1 = pd.read_csv(dataset1, delimiter=",", skiprows=1)
    df2 = pd.read_csv(dataset2, delimiter=",", skiprows=1)
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

        c.execute("SHOW TABLES FROM default")
        tables = c.fetchall()

        for table in tables:
            print(table)
            table_name = table.tableName
            c.execute(f"DROP TABLE IF EXISTS {table_name}")
        
        c.execute("SHOW TABLES FROM default LIKE 'wages_1'")
        result = c.fetchall() 
        print(f"tables: {result}")
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS wages_1 (
                    id int,
                    Country string,
                    Region string,
                    year_2000 DOUBLE,
                    year_2010 DOUBLE,
                    year_2020 DOUBLE
                )
            """
            )
            for _, row in df1.iterrows():
                new_row = []
                for r in row:
                    if r is None:
                        new_row.append("Null")
                    else:
                        new_row.append(r)
                print(new_row)
                convert = (_,) + tuple(new_row)
                c.execute(f"INSERT INTO wages_1 VALUES {convert}")
        c.execute("SHOW TABLES FROM default LIKE 'wages_2'")
        result = c.fetchall()
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS wages_2 (
                    id int,
                    Country string,
                    Region string,
                    year_2022 DOUBLE
                )
            """
            )
            for _, row in df2.iterrows():
                print((_,) + tuple(row))
                convert = (_,) + tuple(row)
                c.execute(f"INSERT INTO wages_2 VALUES {convert}")
        results = c.fetchall()
        print(results)
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
            LIMIT 5
        """)
        results = c.fetchall()
        columns = [desc[0] for desc in c.description]
        filtered_df = pd.DataFrame(results, columns=columns) 
        c.close()

    print(filtered_df)
    
    return filtered_df
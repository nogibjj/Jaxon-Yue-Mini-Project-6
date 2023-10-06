from mylib.operations import (
    close_connection,
    create_wages_data,
    update_wages_data,
    delete_wages_data,
    read_wages_data_by_country,
)
from mylib.loadData import load


def main():
    # Load the dataset into the SQLite database
    load("Development of Average Annual Wages.csv")  # Import data from CSV

    # Create population data with 5-digit numbers
    create_wages_data("China", 10000, 15000, 20000, 22000)

    # Update population data
    update_wages_data("Iceland", 20000, 25000, 30000, 32000)

    # Print population data
    read_wages_data_by_country("China")

    # Delete population data for "Country1"
    delete_wages_data("China")

    # Close the connection
    close_connection()
    return 1


if __name__ == "__main__":
    main()

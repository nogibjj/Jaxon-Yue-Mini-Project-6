# IDS 706 Mini Project 5 [![CI](https://github.com/nogibjj/Jaxon-Yue-Mini-Project-5/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Jaxon-Yue-Mini-Project-5/actions/workflows/cicd.yml)
### Overview
* This repository includes the components for Mini-Project 5 - Python Script interacting with SQL Database.

### Goal
* Builds an ETL-Query pipeline by loading the average annual wages dataset, connecting to a SQL database, and performing CRUD operations.
* Includes SQL queries that **create a new data entry**, **read all countries / individual country's data**, **update data** and **delete data**.

### Key elements in the repository are:
* Development of Average Annual Wages.csv
* lib/loadData.py (for loading the csv file into a SQL database)
* lib/operations.py (for CRUD operations)
* Makefile
* requirements.txt
* Dockerfile
* devcontainer
* main.py
* test_main.py
* GitHub Actions

### Database Connection
`load` function in `lib/loadData.py` would load the data from the csv file into a SQLite database and create a .db file

### CRUD Operations
Functions in `lib/operations.py`:
* `create_wages_data` CREATE: insert a new country's data
* `read_all_wages_data` READ: read all country's data
* `read_wages_data_by_country` READ: read a given country's data
* `update_wages_data` UPDATE: update a given country's data
* `delete_wages_data` DELETE: delete a given country's data

### CRUD in main.py
* **Load csv data into SQLite database**:
`load("Development of Average Annual Wages.csv")`

* **Create new entry for the country China**:
`create_wages_data("China", 10000, 15000, 20000, 22000)`

* **Update Iceland's data**:
`update_wages_data("Iceland", 20000, 25000, 30000, 32000)`

* **Print China's data**
`read_wages_data_by_country("China")`

* **Delete the data for China**
`delete_wages_data("China")`

* **Close the connection**
`close_connection()`

### Results
Successful CRUD Operations
<img width="793" alt="Screenshot 2023-10-02 at 12 28 06 PM" src="https://github.com/nogibjj/Jaxon-Yue-Mini-Project-5/assets/70416390/3b70b8ac-ad57-4318-849f-37e526b5fe9e">

Using Github Actions, I have passed make format, make lint, and make test as shown below.
<img width="809" alt="Screenshot 2023-10-02 at 12 27 34 PM" src="https://github.com/nogibjj/Jaxon-Yue-Mini-Project-5/assets/70416390/fae9bcfb-9367-4a61-a37c-47a8c500c928">


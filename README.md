# IDS 706 Mini Project 6 [![CI](https://github.com/nogibjj/Jaxon-Yue-Mini-Project-5/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Jaxon-Yue-Mini-Project-5/actions/workflows/cicd.yml)
### Overview
* This repository includes the components for Mini-Project 6 - Complex SQL Query for a MySQL Database.

### Goal
* Builds a SQL query pipeline by loading the average annual wages dataset into Databricks and performing a complex SQL query involving joins, aggregation and sorting.

### Key elements in the repository are:
* dataset/Development of Average Annual Wages_1.csv (contains wages info from 2000 to 2020)
* dataset/Development of Average Annual Wages_2.csv (contains wages info from 2022)
* mylib/loadData.py (loading/querying the dataset)
* .env (hidden)
* Makefile
* requirements.txt
* Dockerfile
* devcontainer
* main.py
* test_main.py
* GitHub Actions

### Databricks Connection
Using Databricks thorugh Azura, I created a cluster and retrieved the respective `SERVER_HOSTNAME`, `HTTP_PATH` and `TOKEN`. I stored these in my `.env` file and used them in my load function to connect to Databricks. I also added these three variables to the Action Secrets in the repo settings.

### Complex SQL query
Below is the complex SQL query, which can be found in `mylib/loadData.py`
```
SELECT w1.Region, w1.Country, w1.year_2000, w1.year_2010, w1.year_2020, w2.year_2022, AVG(w2.year_2022) OVER(PARTITION BY w1.Region) as avg_year_2022
FROM wages_1 w1
JOIN wages_2 w2 ON w1.Country = w2.Country
ORDER BY avg_year_2022 DESC, w1.Country
LIMIT 5
```
This query retrieves the top 5 countries with the highest average 2022 wages, grouped by their respective regions. The results include various wage details from the years 2000, 2010, 2020 and 2022 for these countries.

### Results
The resulting dataframe from the SQL query

Using Github Actions, I have passed make format, make lint, and make test as shown below.

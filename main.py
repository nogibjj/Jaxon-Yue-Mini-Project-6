from mylib.loadData import load_table


def main():
    load_table("dataset/Development of Average Annual Wages_1.csv", "wages_1", ["Country TEXT", "Region TEXT", "year_2000 DOUBLE", "year_2010 DOUBLE", "year_2020 DOUBLE"])
    load_table("dataset/Development of Average Annual Wages_2.csv", "wages_2", ["Country TEXT", "Region TEXT", "year_2022 DOUBLE"])

if __name__ == "__main__":
    main()

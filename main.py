from mylib.loadData import load_table
from mylib.loadData import query


def main():
    # load_table("dataset/Development of Average Annual Wages_1.csv", "wages_1", ["id int", "Country STRING", "Region STRING", "year_2000 DOUBLE", "year_2010 DOUBLE", "year_2020 DOUBLE"])
    load_table()
    result = query()
    print("done")  
    import pdb
    pdb.set_trace()
if __name__ == "__main__":
    main()

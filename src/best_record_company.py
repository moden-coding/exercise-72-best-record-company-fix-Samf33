#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    print(df)
    df1= df.groupby("Publisher")["WoC"].sum()
    publisher = df1.idxmax()
    mask = df["Publisher"] == publisher
    return df[mask]

def main():
    print(best_record_company())
    

if __name__ == "__main__":
    main()

import pandas as pd

csvfile = "pred-sweep-2008-2009"

df = pd.read_csv(csvfile + ".csv")


df["year"] = df.iloc[:, 0].apply(str).str[0:4]
dfgp = df.groupby("year")
years = list(dfgp.groups.keys())


def process_df(i_df):

    i_df['sum'] = i_df.iloc[:, 1:].sum(axis=1, skipna=True)
    i_df.sort_values('sum', ascending=False)
    i_df["count"] = i_df.count(axis='columns') - 3
    i_df["fraction"] = i_df['sum'] / i_df['count']
    i_df = i_df.sort_values('sum', ascending=False)
    return i_df



for i in range(len(dfgp.groups)):
    current_df = list(dfgp)[i][1]
    p_df = process_df(current_df)
    p_df.to_csv(years[i]+"-processed.csv")



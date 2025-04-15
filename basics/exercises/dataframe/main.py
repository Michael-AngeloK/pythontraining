import pandas as pd

def main():
    df = pd.read_csv("")
    # print(f"Number of rows are {df.shape[0]} and columns are {df.shape[1]}")

    # print(df.area_type.unique())

    # print(df["size"].unique())

    # print(df[(df["size"] == '2 BHK') & (df["area_type"] == 'Super built-up  Area')])

    # df['price_category'] = df.apply(lambda x: "Affordable" if x['price'] < 80 else "High Cost", axis=1)

    # print(df[df['price'] > df['price'].mean()])

if __name__ == "__main__":
    main()
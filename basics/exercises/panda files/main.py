import pandas as pd

def main():
    df = pd.read_csv("")

    df["year_classify"] = df.apply(lambda x: "before 2000" if x["release_year"] < 2000 else "From 2000", axis=1)

    df.to_csv('final_movie_data.csv', columns=['movie_id', 'title', 'budget', 'revenue', 'year_classify'], index=False)

    df.head(5)

if __name__ == "__main__":
    main()
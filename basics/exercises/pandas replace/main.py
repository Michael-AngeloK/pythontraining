import pandas as pd

df = pd.DataFrame({
})

print(df.shape)

new_df = df.replace(["5%", "10%"], "13%")

new_df = df.replace({
    'Excellent': 4,
    'Very Good': 3,
    'Good': 2,
    'Average': 1
})

print(new_df)
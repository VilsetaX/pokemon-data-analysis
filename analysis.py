import pandas as pd

url = "https://raw.githubusercontent.com/veekun/pokedex/master/pokedex/data/csv/pokemon.csv"

df = pd.read_csv(url)

print("Total Pokemon:", len(df))

print("\nFirst 10 Pokemon:")
print(df[['identifier','height','weight']].head(10))

print("\nAverage Height:", df['height'].mean())
print("Average Weight:", df['weight'].mean())

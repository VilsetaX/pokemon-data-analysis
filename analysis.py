import pandas as pd
import matplotlib.pyplot as plt

# load datasets
stats = pd.read_csv("data/pokemon_stats.csv")
rankings = pd.read_csv("data/great_league_rankings.csv")

# normalize pokemon names for merging
stats["name"] = stats["name"].str.lower()
rankings["pokemon"] = rankings["pokemon"].str.lower()

# merge stats with PvP rankings
df = rankings.merge(
    stats,
    left_on="pokemon",
    right_on="name",
    how="left"
)

# compute total stats
df["total_stats"] = df["attack"] + df["defense"] + df["stamina"]

print("Top ranked Pokémon with stats")
print(df.head())

print("\nAverage stats among top PvP Pokémon")
print(df[["attack", "defense", "stamina"]].mean())

# scatter plot attack vs defense
plt.figure()

plt.scatter(df["attack"], df["defense"])

plt.title("Attack vs Defense in Great League Pokémon")
plt.xlabel("Attack")
plt.ylabel("Defense")

plt.savefig("output/attack_vs_defense.png")

# stamina distribution
plt.figure()

plt.hist(df["stamina"], bins=20)

plt.title("Stamina Distribution Among Top PvP Pokémon")

plt.savefig("output/stamina_distribution.png")

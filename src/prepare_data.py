import pandas as pd

# Charger les fichiers CSV
fake = pd.read_csv("../data/Fake.csv")
true = pd.read_csv("../data/True.csv")

# Ajouter une colonne 'label' : 1 = fake, 0 = real
fake["label"] = 1
true["label"] = 0

# Combiner les deux datasets
df = pd.concat([fake, true])
df = df.sample(frac=1).reset_index(drop=True)  # mélange aléatoire

# Sauvegarder le fichier final
df.to_csv("../data/fake_news.csv", index=False)

print("✅ Dataset combiné enregistré dans data/fake_news.csv")
print(df.head())

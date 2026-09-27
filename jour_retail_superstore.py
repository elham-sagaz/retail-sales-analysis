import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("superstore.csv", encoding='ISO-8859-1')
print(df.columns)
print(df.shape)
# Vérifier valeurs manquantes et doublons
print(df.isna().sum())
print(df.duplicated().sum())
# Supprimer les colonnes inutiles pour l'analyse (identifiants techniques)
df = df.drop(columns=['Row ID', 'Customer ID', 'Product ID', 'Postal Code'])
df['Order Date'] = pd.to_datetime(df['Order Date'])
print(df['Order Date'].dtype)  # doit afficher datetime64
print(df.groupby('Category')[['Sales', 'Profit']].sum())
print(df.groupby('Category')['Discount'].mean())
print(df.groupby('Sub-Category')[['Sales', 'Profit']].sum().sort_values('Profit'))
print(df.groupby('Sub-Category')['Discount'].mean().sort_values(ascending=False))
marge_par_sous_categorie = df.groupby('Sub-Category')[['Sales', 'Profit']].sum()
marge_par_sous_categorie['Marge_%'] = (marge_par_sous_categorie['Profit'] / marge_par_sous_categorie['Sales']) * 100
print(marge_par_sous_categorie.sort_values('Marge_%'))
df['Mois'] = df['Order Date'].dt.month
df['Annee'] = df['Order Date'].dt.year
ventes_mensuelles = df.groupby(['Annee', 'Mois'])['Sales'].sum()
plt.figure(figsize=(12, 5))
ventes_mensuelles.plot(kind='line', marker='o')
plt.title("Évolution des ventes mensuelles")
plt.xlabel("Année, Mois")
plt.ylabel("Ventes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
ventes_par_mois = df.groupby('Mois')['Sales'].mean()
print(ventes_par_mois)
plt.figure(figsize=(10, 5))
ventes_par_mois.plot(kind='bar')
plt.title("Ventes moyennes par mois (toutes années confondues)")
plt.xlabel("Mois")
plt.ylabel("Ventes moyennes")
plt.show()
volume_par_mois = df.groupby('Mois')['Sales'].sum()

plt.figure(figsize=(10, 5))
volume_par_mois.plot(kind='bar')
plt.title("Total des ventes par mois (toutes années confondues)")
plt.xlabel("Mois")
plt.ylabel("Ventes totales")
plt.show()
print(df.groupby('Region')[['Sales', 'Profit']].sum())
print(df.groupby('Segment')[['Sales', 'Profit']].sum())
croise = df.groupby(['Region', 'Category'])['Profit'].sum()
print(croise)

# --- Export des résultats numériques en Excel (plusieurs onglets) ---
with pd.ExcelWriter("analyse_retail_resultats.xlsx") as writer:
    df.groupby('Category')[['Sales', 'Profit']].sum().to_excel(writer, sheet_name='Par_Categorie')
    df.groupby('Sub-Category')[['Sales', 'Profit']].sum().sort_values('Profit').to_excel(writer, sheet_name='Par_SousCategorie')
    marge_par_sous_categorie.to_excel(writer, sheet_name='Marges_pct')
    df.groupby('Region')[['Sales', 'Profit']].sum().to_excel(writer, sheet_name='Par_Region')
    df.groupby('Segment')[['Sales', 'Profit']].sum().to_excel(writer, sheet_name='Par_Segment')
    df.groupby(['Region', 'Category'])['Profit'].sum().to_excel(writer, sheet_name='Region_x_Categorie')
    volume_par_mois.to_excel(writer, sheet_name='Ventes_par_mois')

print("Fichier Excel exporté avec succès !")

# --- Export des graphiques en images PNG ---

plt.figure(figsize=(8, 5))
df.groupby('Category')[['Sales', 'Profit']].sum().plot(kind='bar')
plt.title("Ventes et profit par catégorie")
plt.ylabel("Montant")
plt.tight_layout()
plt.savefig("1_ventes_profit_categorie.png", dpi=300, bbox_inches='tight')
plt.close()

plt.figure(figsize=(10, 6))
sns.barplot(data=marge_par_sous_categorie.reset_index(), x='Marge_%', y='Sub-Category')
plt.title("Marge (%) par sous-catégorie")
plt.tight_layout()
plt.savefig("2_marge_sous_categorie.png", dpi=300, bbox_inches='tight')
plt.close()

plt.figure(figsize=(12, 5))
ventes_mensuelles.plot(kind='line', marker='o')
plt.title("Évolution des ventes mensuelles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("3_evolution_mensuelle.png", dpi=300, bbox_inches='tight')
plt.close()

plt.figure(figsize=(10, 5))
volume_par_mois.plot(kind='bar')
plt.title("Total des ventes par mois (saisonnalité)")
plt.tight_layout()
plt.savefig("4_saisonnalite.png", dpi=300, bbox_inches='tight')
plt.close()

plt.figure(figsize=(8, 5))
df.groupby('Region')[['Sales', 'Profit']].sum().plot(kind='bar')
plt.title("Ventes et profit par région")
plt.tight_layout()
plt.savefig("5_region.png", dpi=300, bbox_inches='tight')
plt.close()

# --- Export du dataset nettoyé ---
df.to_csv("superstore_nettoye.csv", index=False)

print("Tous les graphiques et fichiers ont été exportés !")


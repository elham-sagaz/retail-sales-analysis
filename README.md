# Analyse des Ventes — Secteur Retail (Superstore)

## Contexte et objectif

Ce projet analyse 9 994 commandes d'un magasin retail afin d'identifier les leviers de rentabilité et les tendances de vente, et de proposer des recommandations business concrètes.

**Source des données** : Superstore Dataset (Kaggle)
**Outils utilisés** : Python (pandas, numpy, matplotlib, seaborn)

## Méthodologie

1. Exploration et vérification de la qualité des données (aucune valeur manquante, aucun doublon détecté)
2. Conversion des dates et extraction du mois/année pour l'analyse temporelle
3. Analyse de la rentabilité par catégorie, sous-catégorie et calcul de marges réelles (%)
4. Analyse de l'impact des remises sur la rentabilité
5. Analyse de la saisonnalité des ventes
6. Analyse croisée région × catégorie × segment client

## Résultats clés

### 1. Le Furniture génère des ventes élevées mais une rentabilité très faible
Le Furniture représente 742 000 en ventes (quasi équivalent aux autres catégories), mais seulement 18 451 de profit — une marge de 2.5%, contre 17% pour les deux autres catégories.

### 2. Deux sous-catégories précises sont en perte nette
**Tables** (marge de -8.6%) et **Bookcases** (-3.0%) sont les seules sous-catégories déficitaires du magasin, expliquant à elles seules la faible rentabilité du Furniture.

### 3. La remise n'explique pas tout — la marge de base du produit compte davantage
Binders bénéficie de la remise moyenne la plus élevée du magasin (37.2%) tout en restant rentable (marge 14.9%), alors que Tables devient déficitaire avec une remise plus modérée (26.1%). La rentabilité dépend de la combinaison remise + marge de base, pas de la remise seule.

### 4. Le problème du Furniture est concentré dans une seule région
Sur les 4 régions du magasin, seule la région **Central** affiche une perte nette sur le Furniture (-2 871). Les 3 autres régions parviennent à maintenir cette catégorie rentable, même modestement.

### 5. Fortes ventes saisonnières, sans hausse du panier moyen
Le volume de ventes est nettement plus élevé en septembre et au dernier trimestre (novembre-décembre), avec un pic à 355 000 en novembre contre 60 000 en février. Le panier moyen par commande, lui, reste stable toute l'année — la saisonnalité s'explique donc par le nombre de commandes, pas par leur valeur individuelle.

### 6. La région West et le segment Consumer sont les moteurs de performance
La région West génère à la fois le meilleur volume de ventes et la meilleure marge (14.9%). Le segment Consumer domine largement en ventes et en profit face aux segments Corporate et Home Office.

## Recommandations

1. **Revoir la politique de prix ou de remise du Furniture spécifiquement en région Central**, seule zone où cette catégorie est déficitaire — plutôt qu'une action globale sur toute la catégorie
2. **Réévaluer la stratégie de remise sur Tables et Bookcases**, les deux seules sous-catégories structurellement non rentables
3. **Renforcer les stocks et les actions marketing en septembre et au dernier trimestre**, périodes de forte demande identifiées
4. **Étudier les facteurs de succès de la région West** pour évaluer leur reproductibilité dans les autres régions, notamment Central

---

# Sales Analysis — Retail Sector (Superstore)

## Context and objective

This project analyzes 9,994 orders from a retail store to identify profitability drivers and sales trends, and to propose concrete business recommendations.

**Data source**: Superstore Dataset (Kaggle)
**Tools used**: Python (pandas, numpy, matplotlib, seaborn)

## Methodology

1. Data exploration and quality checks (no missing values, no duplicates found)
2. Date conversion and month/year extraction for time-based analysis
3. Profitability analysis by category, sub-category, and calculation of real profit margins (%)
4. Analysis of discount impact on profitability
5. Seasonality analysis of sales volume
6. Cross-analysis of region × category × customer segment

## Key findings

### 1. Furniture generates high sales but very low profitability
Furniture accounts for 742,000 in sales (nearly on par with other categories) but only 18,451 in profit — a 2.5% margin, compared to 17% for the other two categories.

### 2. Two specific sub-categories are running at a net loss
**Tables** (-8.6% margin) and **Bookcases** (-3.0%) are the only loss-making sub-categories in the store, and alone explain Furniture's weak overall profitability.

### 3. Discount alone doesn't explain profitability — base product margin matters more
Binders carries the store's highest average discount (37.2%) yet remains profitable (14.9% margin), while Tables turns unprofitable with a more moderate discount (26.1%). Profitability depends on the combination of discount and base margin, not discount alone.

### 4. Furniture's problem is concentrated in a single region
Of the store's 4 regions, only **Central** shows a net loss on Furniture (-2,871). The other three regions manage to keep this category profitable, even if modestly.

### 5. Strong seasonal sales volume, without a higher average order value
Sales volume is markedly higher in September and the last quarter (November-December), peaking at 355,000 in November versus 60,000 in February. The average order value, however, stays stable year-round — seasonality is therefore driven by order count, not by individual order value.

### 6. The West region and Consumer segment are the top performers
The West region delivers both the highest sales volume and the best margin (14.9%). The Consumer segment clearly dominates in both sales and profit over Corporate and Home Office.

## Recommendations

1. **Revisit Furniture pricing or discount policy specifically in the Central region**, the only zone where this category runs at a loss — rather than a blanket change across the whole category
2. **Reassess the discount strategy on Tables and Bookcases**, the only two structurally unprofitable sub-categories
3. **Strengthen inventory and marketing efforts in September and the last quarter**, the periods of identified peak demand
4. **Study the success factors behind the West region's performance** to assess whether they can be replicated in other regions, particularly Central

# Boutik

Boutik est la boutique en ligne de notre startup : un petit programme Python, en ligne de commande, pour consulter un catalogue de produits tech, remplir un panier et passer commande.

> Projet pédagogique de la formation **Git & GitHub**. Chaque table d'élèves forme une startup qui fait évoluer Boutik, de la v0.1.0 (prototype buggé) à la v1.0.0.

## Fonctionnalités (v0.1.0)

- Afficher le catalogue et rechercher un produit
- Ajouter et retirer des produits du panier
- Afficher la facture et valider la commande (le stock est mis à jour)

## Installation

Prérequis : **Python 3.9 ou plus** et **Git**.

```bash
git clone <url-du-depot>
cd <nom-du-depot>
pip install -r requirements.txt     # installe pytest (facultatif)
```

## Lancer la boutique

```bash
python main.py          # Windows : py main.py
```

## Lancer les tests

```bash
python -m pytest        # avec pytest
python run_tests.py     # sans rien installer
```

Les tests se lancent aussi automatiquement sur GitHub à chaque push et à chaque Pull Request (onglet **Actions**).

## Structure du projet

```
├── boutik/
│   ├── catalog.py      # catalogue : chargement, recherche
│   ├── cart.py         # panier
│   ├── pricing.py      # TVA, promos, livraison
│   ├── stock.py        # stock
│   ├── invoice.py      # facture
│   └── cli.py          # menu en ligne de commande
├── data/products.csv   # les produits
├── tests/              # les tests automatiques
├── main.py             # point d'entrée
└── run_tests.py        # lance les tests sans pytest
```

## Contribuer

Lis [CONTRIBUTING.md](CONTRIBUTING.md) : une issue, une branche, une Pull Request relue.

## Équipe

| Rôle | Nom | GitHub |
| --- | --- | --- |

## Licence

[MIT](LICENSE)

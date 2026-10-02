"""Catalogue : chargement, recherche et affichage des produits."""

import csv
from pathlib import Path

DEFAULT_PATH = Path(__file__).resolve().parent.parent / "data" / "products.csv"


def load_products(path=DEFAULT_PATH):
    """Charge les produits du fichier CSV et renvoie une liste de dictionnaires."""
    products = []
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            products.append({
                "id": int(row["id"]),  # <-- Conversion en int ici
                "name": row["name"],
                "category": row["category"],
                "price_ht": float(row["price_ht"]),
                "stock": int(row["stock"]),
            })
    return products

def find_product(products, product_id):
    """Renvoie le produit qui a cet identifiant, ou None s'il n'existe pas."""
    for product in products:
        if product["id"] == product_id:
            return product
    return None


def search(products, text):
    """Renvoie les produits dont le nom contient le texte recherché."""
    return [p for p in products if text in p["name"]]


# TODO (mission F3) : ajouter ici la fonction filter_by_category(products, category)


def categories(products):
    """Renvoie la liste triée des catégories du catalogue."""
    return sorted({p["category"] for p in products})


# TODO (mission F6) : ajouter ici la fonction sort_by_price(products, descending=False)

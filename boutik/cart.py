"""Panier : un dictionnaire {id_produit: quantité}."""

from boutik.catalog import find_product
from boutik.pricing import price_ttc


def add_to_cart(cart, product_id, quantity=1):
    """Ajoute `quantity` exemplaires du produit au panier."""
    cart[product_id] = cart.get(product_id, 0) + quantity


def remove_from_cart(cart, product_id):
    """Retire complètement un produit du panier."""
    del cart[product_id]


def cart_count(cart):
    """Renvoie le nombre total d'articles dans le panier."""
    return sum(cart.values())


def cart_total(cart, products):
    """Renvoie le montant total TTC du panier, arrondi au centime."""
    total = 0
    for product_id, quantity in cart.items():
        product = find_product(products, product_id)
        total += price_ttc(product["price_ht"]) * quantity
    return round(total, 2)

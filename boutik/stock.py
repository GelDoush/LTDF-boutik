"""Stock : disponibilité et réservation des produits."""


def is_available(product, quantity):
    """Indique si on peut vendre `quantity` exemplaires de ce produit."""
    return product["stock"] >= quantity


def reserve(product, quantity):
    """Retire `quantity` exemplaires du stock (erreur si le stock est insuffisant)."""
    if not is_available(product, quantity):
        raise ValueError(f"Stock insuffisant pour {product['name']}")
    product["stock"] -= quantity


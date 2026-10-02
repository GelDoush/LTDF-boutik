"""Stock : disponibilité et réservation des produits."""


def is_available(product, quantity):
    """Indique si on peut vendre `quantity` exemplaires de ce produit."""
    return product["stock"] >= quantity


def reserve(product, quantity):
    """Retire `quantity` exemplaires du stock (erreur si le stock est insuffisant)."""
    if not is_available(product, quantity):
        raise ValueError(f"Stock insuffisant pour {product['name']}")
    product["stock"] -= quantity

def low_stock(products, threshold=3):
    """Renvoie la liste des produits dont le stock est inférieur ou égal à `threshold`."""
    for i in products:
        if i["stock"] <= threshold:
            yield i
    

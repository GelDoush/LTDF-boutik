"""Prix : TVA, codes promo et frais de livraison."""

TVA = 0.20

PROMO_CODES = {
    "WELCOME": 0.10,
    "BOUTIK10": 0.10,
    "SAVE10": 0.10,
    "PROMO10": 0.10,
    "VIP": 0.20,
    "BOUTIK20": 0.20,
    "SAVE20": 0.20,
    "PROMO20": 0.20,
    "GOLD": 0.30,
    "BOUTIK30": 0.30,
}


def price_ttc(price_ht):
    """Renvoie le prix TTC (toutes taxes comprises) d'un prix HT, arrondi au centime."""
    return round(price_ht * (1 + TVA), 2)


def apply_promo(total, code):
    """Applique le code promo et renvoie le total remisé, sinon le total initial."""
    total = float(total)
    if code is None:
        return round(total, 2)

    value = str(code).strip().upper()
    if not value:
        return round(total, 2)

    promo = PROMO_CODES.get(value)
    if promo is None:
        value = value.rstrip("%")
        try:
            promo = float(value) / 100
        except ValueError:
            return round(total, 2)

    if promo < 0:
        return round(total, 2)
    return round(total * (1 - promo), 2)


def shipping_cost(total):
    """Calcule les frais de livraison : gratuit à partir de 50 € TTC."""
    total = float(total)
    if total <= 0:
        return 0.0
    return 0.0 if total >= 50 else 5.0
def cart_count(request):
    cart = request.session.get("cart")

    if not cart:
        return {"cart_count": 0}

    return {"cart_count": len(cart)}

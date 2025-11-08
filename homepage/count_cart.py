
# This handles the count items on the cart when user selects services to book


def cart_count(request):
    cart = request.session.get('cart', {})
    return {'cart_count': len(cart)}

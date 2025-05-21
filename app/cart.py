from .models import Cart, Product

def get_cart_items(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key
    return Cart.objects.filter(session_key=session_key)

def add_product_to_cart(request, product_id):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    product = Product.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(
        session_key=session_key,
        product=product,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
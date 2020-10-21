from django.shortcuts import render
from .models import Cart, Product, CartProduct

# Create your views here.


def home(request):
    cart = Cart.objects.get(id=1)
    products = Product.objects.all().order_by('-priority')

    if request.method == "POST":
        product_selected = Product.objects.get(id=request.POST['product_id'])
        cart_product = CartProduct(cart=cart, product=product_selected)
        cart_product.save()
        cart.products_counter = len(CartProduct.objects.all().filter(cart=cart))
        cart.save()
    context = {
        'cart': cart,
        'products': products,
    }
    return render(request, 'pages/home.html', context)

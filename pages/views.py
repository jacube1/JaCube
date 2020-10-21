from django.shortcuts import render
from .models import Cart, Product, CartProduct

# Create your views here.


def home(request):
    cart = Cart.objects.get(id=1)
    products = Product.objects.all().order_by('-priority')
    cart_products = CartProduct.objects.all().filter(cart=cart)

    if request.method == "POST":
        product_selected = Product.objects.get(id=request.POST['product_id'])
        try:
            cart_product = CartProduct.objects.get(cart=cart, product=product_selected)
        except CartProduct.DoesNotExist:
            cart_product = CartProduct(cart=cart, product=product_selected, amount=0)
        cart_product.amount += 1
        cart_product.save()
        cart.products_counter = sum([p.amount for p in cart_products])
        cart.save()
    context = {
        'cart_products': cart_products,
        'cart': cart,
        'products': products,
    }
    return render(request, 'pages/home.html', context)


def cart_submit(request):
    return render(request, 'pages/cart_submit.html')

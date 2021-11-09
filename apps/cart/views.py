from django.shortcuts import render, redirect

from apps.cart.cart import Cart


def cart_detail(request):
    cart = Cart(request)
    remove_from_cart = request.GET.get('remove_from_cart', '')

    if remove_from_cart:
        cart.remove(remove_from_cart)

        return redirect('cart')
    return render(request, 'cart/cart.html')

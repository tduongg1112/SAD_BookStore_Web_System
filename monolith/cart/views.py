from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from .forms import CartForm, CartItemForm

def cart_list(request):
    carts = Cart.objects.all()
    return render(request, 'cart/cart_list.html', {'carts': carts})

def cart_create(request):
    form = CartForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cart_list')
    return render(request, 'cart/cart_form.html', {'form': form})

def cart_update(request, pk):
    cart = get_object_or_404(Cart, pk=pk)
    form = CartForm(request.POST or None, instance=cart)
    if form.is_valid():
        form.save()
        return redirect('cart_list')
    return render(request, 'cart/cart_form.html', {'form': form})

def cart_delete(request, pk):
    cart = get_object_or_404(Cart, pk=pk)
    if request.method == 'POST':
        cart.delete()
        return redirect('cart_list')
    return render(request, 'cart/cart_confirm_delete.html', {'object': cart})

def cartitem_list(request):
    cartitems = CartItem.objects.all()
    return render(request, 'cart/cartitem_list.html', {'cartitems': cartitems})

def cartitem_create(request):
    form = CartItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cartitem_list')
    return render(request, 'cart/cartitem_form.html', {'form': form})

def cartitem_update(request, pk):
    cartitem = get_object_or_404(CartItem, pk=pk)
    form = CartItemForm(request.POST or None, instance=cartitem)
    if form.is_valid():
        form.save()
        return redirect('cartitem_list')
    return render(request, 'cart/cartitem_form.html', {'form': form})

def cartitem_delete(request, pk):
    cartitem = get_object_or_404(CartItem, pk=pk)
    if request.method == 'POST':
        cartitem.delete()
        return redirect('cartitem_list')
    return render(request, 'cart/cartitem_confirm_delete.html', {'object': cartitem})
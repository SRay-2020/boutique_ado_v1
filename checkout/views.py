from django.shortcuts import render, redirect, reverse 
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, "There's nothing in your bag")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JYSDEAQb6q0x2KwgVMPWeio4ynVOjfeAOYiTKJY5j1PuNt9fq5ydDkuAeave2L5qf5YqBphC2KCkmhqzVQ0yQxA00dRAxgEED',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.urls import reverse

from config.settings import STRIPE_SECRET_KEY, STRIPE_PUBLIC_KEY, APP_URL

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Item

import stripe

stripe.api_key = STRIPE_SECRET_KEY

class ItemView(TemplateView):
    template_name = 'item/page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = get_object_or_404(Item, id=context['id'])
        context['item'] = item
        context['stripe_public_key'] = STRIPE_PUBLIC_KEY
        return context

class BuyItemView(APIView):
    def get(self, request, id):
        item = get_object_or_404(Item, id=id)

        view_item_url = f'{APP_URL}{reverse("view-item", args=[id])}'

        session = stripe.checkout.Session.create(
            mode='payment',
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': item.name,
                        },
                        'unit_amount': int(item.price * 100),
                    },
                    'quantity': 1,
                }
            ],
            success_url=view_item_url,
            cancel_url=view_item_url,
        )

        return Response({'sessionId': session.id})
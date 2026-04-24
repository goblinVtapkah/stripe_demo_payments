from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.urls import reverse

from config.settings import STRIPE_KEYS, APP_URL

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Item

import stripe

class ItemView(TemplateView):
	template_name = 'item/item_page.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		item = get_object_or_404(Item, id=context['id'])
		context['stripe_public_key'] = STRIPE_KEYS[item.currency.lower()]['pk']
		if hasattr(item, 'discount'):
			item.price = item.price - (item.price * (item.discount.percent / 100))
		else:
			item.price = item.price
		context['item'] = item
		return context

class ItemsView(TemplateView):
	template_name = 'item/items_page.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		items = Item.objects.all()
		context['items'] = items
		for item in items:
			if hasattr(item, 'discount'):
				item.price = item.price - (item.price * (item.discount.percent / 100))
			else:
				item.price = item.price
		return context

class BuyItemView(APIView):
	def get(self, request, id):
		item = get_object_or_404(Item, id=id)

		view_item_url = f'{APP_URL}{reverse("view-item", args=[id])}'
		
		currency = item.currency.lower()

		stripe.api_key = STRIPE_KEYS[item.currency.lower()]['sk']

		discounts = []
		if hasattr(item, 'discount'):
			coupon = stripe.Coupon.create(
				percent_off=item.discount.percent,
				duration="once",
			)
			discounts.append({
				"coupon": coupon.id
			})
		session = stripe.checkout.Session.create(
			mode='payment',
			line_items=[
				{
					'price_data': {
						'currency': currency,
						'product_data': {
							'name': item.name,
						},
						'unit_amount': int(item.price * 100),
					},
					'quantity': 1,
				}
			],
			discounts=discounts,
			success_url=view_item_url,
			cancel_url=view_item_url,
		)
		
		return Response({ 'sessionId': session.id })
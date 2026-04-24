from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.urls import reverse

from config.settings import STRIPE_KEYS, APP_URL

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, OrderItem
from item.models import Item

from .serializers import CreateOrderSerializer

import stripe

class OrdersView(TemplateView):
	template_name = 'order/orders_page.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['orders'] = Order.objects.all()
		return context

class OrderView(TemplateView):
	template_name = 'order/order_page.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		order = get_object_or_404(Order, id=context['id'])
		items = order.items.all()
		context['items'] = items
		for item in items:
			if hasattr(item.item, 'discount'):
				item.item.price = item.item.price - (item.item.price * (item.item.discount.percent / 100))
			else:
				item.item.price = item.item.price
		context['stripe_public_key'] = STRIPE_KEYS[items[0].item.currency.lower()]['pk']
		return context

class BuyOrderView(APIView):
	def get(self, request, id):
		order = get_object_or_404(Order, id=id)

		view_order_url = f'{APP_URL}{reverse("view-order", args=[id])}'
		
		items = order.items.all()

		currency = items[0].item.currency.lower()
		
		line_items = []

		for item in items:
			line_items.append({
				'price_data': {
					'currency': item.item.currency,
					'product_data': {
						'name': item.item.name,
					},
					'unit_amount': int(item.item.price * 100),
				},
				'quantity': 1,
			})

		stripe.api_key = STRIPE_KEYS[currency]['sk']
		session = stripe.checkout.Session.create(
			mode='payment',
			line_items=line_items,
			success_url=view_order_url,
			cancel_url=view_order_url,
		)
		
		return Response({ 'sessionId': session.id })

class CreateOrderView(APIView):
	def post(self, request):
		serializer = CreateOrderSerializer(data=request.data)

		if serializer.is_valid():
			data = serializer.validated_data

			order = Order.objects.create()
			
			for itemId in data['items']:
				item = Item.objects.get(id=itemId)
				order_item = OrderItem.objects.create(
					order=order,
					item=item,
				)
				
			return Response({
				'orderUrl': reverse('view-order', args=[order.id])
			})

		return Response(serializer.errors, status=400)
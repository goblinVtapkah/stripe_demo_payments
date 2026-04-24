"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from item.views import ItemView, ItemsView, BuyItemView
from order.views import CreateOrderView, OrdersView, OrderView, BuyOrderView

urlpatterns = [
	path('admin/', admin.site.urls),
	path('item/', ItemsView.as_view(), name="view-items"),
	path('item/<int:id>/', ItemView.as_view(), name="view-item"),
	path('buy/<int:id>/', BuyItemView.as_view(), name="buy-item"),
	path('order/create/', CreateOrderView.as_view(), name="create-order"),
	path('order/', OrdersView.as_view(), name="view-orders"),
	path('order/<int:id>/', OrderView.as_view(), name="view-order"),
	path('order/buy/<int:id>/', BuyOrderView.as_view(), name="buy-order")
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home), #page.html
    path('support', views.chatSupport),
    path('store', views.store),
    path('description', views.itemDescription),
    path('cart', views.shoppingCart),
    path('login', views.login),

]

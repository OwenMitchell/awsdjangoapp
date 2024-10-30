from django.urls import path

from . import views


urlpatterns = [
    path('hello/', views.HelloWorld.as_view(), name="hello"),
    path('create-payment-intent/', views.CreatePaymentIntentView.as_view(),
         name='create-payment-intent'),
    path('get-csrf', views.get_csrf, name='get-csrf'),
]

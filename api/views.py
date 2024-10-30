from django.shortcuts import render
from rest_framework.views import APIView, View
from rest_framework.response import Response
from .models import Product, Sale
from .serializers import ProductSerializer
import stripe
from django.http import JsonResponse
from django.conf import settings
from django.middleware.csrf import get_token
import json


class HelloWorld(APIView):
    def get(self, request):
        products = Product.objects.all()
        seralizer = ProductSerializer(products, many=True)
        return Response(seralizer.data)


stripe.api_key = settings.STRIPE_SECRET_KEY


class CreatePaymentIntentView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            amount = data.get('amount')  # amount in cents

            sale = Sale(
                items=data.get('cartItems')
            )

            sale.save()

            # Create a PaymentIntent
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='cad',
            )

            return JsonResponse({
                'clientSecret': intent['client_secret']
            })
        except json.JSONDecodeError as jde:
            return JsonResponse({'jsondecode error': str(jde)}, status=400)
        except Exception as e:
            return JsonResponse({'error': e}, status=400)


def get_csrf(request):
    return JsonResponse({"csrf_token": get_token(request)})

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

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from asgiref.sync import sync_to_async
import asyncio


class HelloWorld(APIView):
    def get(self, request):
        products = Product.objects.all()
        seralizer = ProductSerializer(products, many=True)
        return Response(seralizer.data)


stripe.api_key = settings.STRIPE_SECRET_KEY

@method_decorator(csrf_exempt, name='dispatch')
class CreatePaymentIntentView(View):
    async def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            amount = data.get('amount')  # amount in cents

            # Create a PaymentIntent
            intent = await sync_to_async(stripe.PaymentIntent.create)(
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
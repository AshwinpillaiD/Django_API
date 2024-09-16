from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.decorators import api_view
from .models import (Products,
                     )
from .Serializers import Products_serializers


#Class-based Views

class ProductsView(APIView):
    def post(self, request):
        new_product=Products(products =request.data["products"],code =request.data["code"],price =request.data["price"])
        new_product.save()
        return Response("Data Saved")
    
    def get(self,request):
        all_products=Products.objects.all()
        all_iteam=[]
        
        for products_iteam in all_products:
            single_products={
                                "id": products_iteam.id,
                                "products" : products_iteam.products,
                                "code" : products_iteam.code,
                                "price": products_iteam.price
                            }
            all_iteam.append(single_products)
        
        return Response(all_iteam)
    
class ProductsViewId(APIView):
    def get(self,request,id):
        all_products=Products.objects.get(id = id)
        single_products={
                                "id": all_products.id,
                                "products" : all_products.products,
                                "code" : all_products.code,
                                "price": all_products.price
                        }
        return Response(single_products)
    
    def patch(self,request,id):
        single_product=Products.objects.filter(id = id)
        single_product.update(products =request.data["products"],code =request.data["code"],price =request.data["price"])
        return Response('single_product')
    

    def delete(self,request,id):
        single_product=Products.objects.get(id = id)
        single_product.delete()
        return Response('Deleted')


    def get(self,request):
        all_products=Products.objects.all()
        serializer = Products_serializers(all_products,many=True).data

        return Response(serializer)
    
    def get(self,request,id):
        all_products=Products.objects.get(id = id)
        serializer = Products_serializers(all_products).data

        return Response(serializer)
    

def function_
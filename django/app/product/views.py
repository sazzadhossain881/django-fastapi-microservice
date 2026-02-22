from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product
from product.serializers import ProductSerializer
# Create your views here.

class ProductAPIView(APIView):

    def get(self, request):

        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
        

    def post(self, request):

        try:

            data = request.data
            serializer = ProductSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status": True,
                    "message": "product successfully created",
                    "data": serializer.data
                })
        
        except Exception as e:
            print(e)
            return Response({
                "status": False,
                "message": "something went wrong",
                "data": serializer.errors
            })
    

class productRetrieveAPIView(APIView):
     def get(self, request, product_id):

        try:
            product = Product.objects.get(id=product_id)

        except Product.DoesNotExist:
            return Response({
                "status": False,
                "message": "product not found",
                "data": {}
            })
        
        serializer = ProductSerializer(product, many=False)
        return Response({
            "status": True,
            "message": "product fetched",
            "data": serializer.data
        })

class ProductupdateAPIView(APIView):
     
     def patch(self, request, product_id):

        try:
            data = request.data
            if not product_id:
                return Response({
                    "status": False,
                    "message": "product id required",
                    "data": {}
                })
            

            product_obj = Product.objects.filter(id=product_id)
            if product_obj.exists():
                serializer = ProductSerializer(product_obj[0], data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        "status": True,
                        "message": "product updated successfully",
                        "data": serializer.data
                    })
                
                return Response({
                    "status": False,
                    "message": "product not updated",
                    "data": serializer.errors
                })
            

            return Response({
                "status": False,
                "message": "invalid product id",
                "data": {}
            })
        
        except Exception as e:
            print(e)
            return Response({
                "status": False,
                "message": "something went wrong",
                "data": {}
            })

class ProductDeleteAPIView(APIView):

    def delete(self, request, product_id):

        try:
            if not product_id:
                return Response({
                    "status": False,
                    "message": "product id required",
                    "data": {}
                })
            try:
                product = Product.objects.get(id=product_id)
                product.delete()
                return Response({
                    "status": True,
                    "message": "product deleted successfully",
                    "data": {}
                })
            
            except Exception as e:
                print(e)
                return Response({
                    "status": True,
                    "message": "invalid product id",
                    "data": {}
                })
        
        except Exception as e:
            print(e)
            return Response({
                "status": False,
                "message": "something went wrong",
                "data": {}
            })
        

                
        


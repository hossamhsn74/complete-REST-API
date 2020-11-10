from ..models import Product
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import permissions
# from rest_framework.schemas import AutoSchema
# import coreapi


# class ProductViewSchema(AutoSchema):
#     def get_manual_fields(self, path, method):
#         extra_fields = []
#         if method.lower() in ['post', 'put']:
#             extra_fields = [
#                 coreapi.Field['descreption']
#             ]
#         manual_fields = super().get_manual_fields(path, method)
#         return manual_fields + extra_fields


class ProductListView(generics.ListAPIView):
    """
    View to list all products in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    # schema = ProductViewSchema


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    # schema = ProductViewSchema

    def create(self, request, *args, **kwargs):
        super(ProductCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        return Response(response)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    # schema = ProductViewSchema

    def retrieve(self, request, *args, **kwargs):
        super(ProductDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(ProductDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "result": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(ProductDetailView, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully deleted"}
        return Response(response)

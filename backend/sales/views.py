from rest_framework import viewsets
from .models import Product, Invoice,Sale
from .serializers import ProductSerializer, InvoiceSerializer, SaleSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum
from django_filters import rest_framework as filters

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]

class ProductFilter(filters.FilterSet):
    store_name = filters.CharFilter(field_name='store__store_name', lookup_expr='icontains')
    city = filters.CharFilter(field_name='store__city', lookup_expr='icontains')
    zip_code = filters.CharFilter(field_name='store__zip_code', lookup_expr='exact')
    county_number = filters.NumberFilter(field_name='store__county_number')
    county = filters.CharFilter(field_name='store__county', lookup_expr='icontains')
    category_name = filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    vendor_name = filters.CharFilter(field_name='vendor_name', lookup_expr='icontains')
    item_number = filters.CharFilter(field_name='item_number', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['store_name', 'city', 'zip_code', 'county_number', 'county', 'category_name', 'vendor_name', 'item_number']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        
        # Total sales amount (sum of sale_amount)
        total_sales = queryset.aggregate(total_sales=Sum('sale_amount'))['total_sales'] or 0
        
        # Total profit (sum of profit)
        total_profit = queryset.aggregate(total_profit=Sum('profit'))['total_profit'] or 0
        
        return Response({
            'total_sales': total_sales,
            'total_profit': total_profit,
            'sales_data': SaleSerializer(queryset, many=True).data
        })

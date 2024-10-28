from rest_framework import serializers
from .models import Product, Invoice,Sale, Store, Category

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    store_name = serializers.CharField(source='store.store_name', read_only=True)  
    vendor_name = serializers.CharField(source='vendor.vendor_name', read_only=True) 
    category_name = serializers.CharField(source='category.name', read_only=True) 

    class Meta:
        model = Product
        fields = [
            'invoice_item_number',
            'date',
            'store_number',
            'store_name',
            'address',
            'city',
            'zip_code',
            'store_location',
            'county_number',
            'county',
            'category',
            'category_name',
            'vendor_number',
            'vendor_name',
            'item_number',
            'item_desc',
            'pack',
            'bottle_volume_ml',
            'state_bottle_cost',
            'state_bottle_retail',
            'bottles_sold',
            'sale_dollars',
            'volume_sold_liters',
            'volume_sold_gallons',
        ]

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

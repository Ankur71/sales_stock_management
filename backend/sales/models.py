from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    category_name = models.CharField(max_length=100)  # Added based on your request


    def __str__(self):
        return self.name

class Vendor(models.Model):
    vendor_number = models.CharField(max_length=100)
    vendor_name = models.CharField(max_length=255)

    def __str__(self):
        return self.vendor_name

class Store(models.Model):
    store_name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    county_number = models.IntegerField()
    county = models.CharField(max_length=100)
    store_location = models.CharField(max_length=255)  # Adjusted to match provided name


    def __str__(self):
        return self.store_name

class Product(models.Model):
    invoice_item_number = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    store_number = models.CharField(max_length=50, null=True, blank=True)
    store_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    store_location = models.CharField(max_length=100, null=True, blank=True)
    county_number = models.IntegerField(null=True, blank=True)
    county = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)  # or ForeignKey to a Category model
    category_name = models.CharField(max_length=100, null=True, blank=True)
    vendor_number = models.CharField(max_length=50, null=True, blank=True)
    vendor_name = models.CharField(max_length=100, null=True, blank=True)
    item_number = models.CharField(max_length=50, null=True, blank=True)
    item_desc = models.TextField(null=True, blank=True)
    pack = models.CharField(max_length=50, null=True, blank=True)
    bottle_volume_ml = models.PositiveIntegerField(null=True, blank=True)
    state_bottle_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    state_bottle_retail = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    bottles_sold = models.IntegerField(null=True, blank=True)
    sale_dollars = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    volume_sold_liters = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    volume_sold_gallons = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.item_number
    
class Invoice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True,)
    quantity = models.PositiveIntegerField(null=True, blank=True)  
    date = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.product.state_bottle_cost * self.quantity  
    
class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True,)
    item_name = models.CharField(max_length=255)
    sale_amount = models.DecimalField(max_digits=10, decimal_places=2)
    profit = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    @property
    def total_price(self):
        return self.sale_amount 

import csv
from django.core.management.base import BaseCommand
from sales.models import Product  # Adjust the import based on your app name
from datetime import datetime

class Command(BaseCommand):
    help = 'Import products from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file to import')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if 'date' in row and row['date']:
                        date_str = row['date']
                        date_obj = datetime.strptime(date_str, '%d-%m-%Y')  # Updated format
                        row['date'] = date_obj.date()
                if 'bottle_volume_ml' in row:
                    row['bottle_volume_ml'] = row['bottle_volume_ml'].replace(',', '')

                if 'state_bottle_cost' in row:
                        row['state_bottle_cost'] = row['state_bottle_cost'].replace(',', '')

                if 'bottles_sold' in row:
                    row['bottles_sold'] = row['bottles_sold'].replace(',', '')
                
                if 'sale_dollars' in row and row['sale_dollars']:
                        row['sale_dollars'] = float(row['sale_dollars'].replace(',', ''))

                county_number = row.get('county_number', None)
                if county_number in (None, '', 'null'):
                    county_number = 0
                else:
                    county_number = int(county_number)


                product = Product(
                    invoice_item_number=row['invoice_item_number'],
                    date=row['date'],
                    store_number=row['store_number'],
                    store_name=row['store_name'],
                    address=row['address'],
                    city=row['city'],
                    zip_code=row['zip_code'],
                    store_location=row['store_location'],
                    county_number=county_number,
                    county=row['county'],
                    category=row['category'],
                    category_name=row['category_name'],
                    vendor_number=row['vendor_number'],
                    vendor_name=row['vendor_name'],
                    item_number=row['item_number'],
                    item_desc=row['item_desc'],
                    pack=row['pack'],
                    bottle_volume_ml=row['bottle_volume_ml'],
                    state_bottle_cost=row['state_bottle_cost'],
                    state_bottle_retail=row['state_bottle_retail'],
                    bottles_sold=row['bottles_sold'],
                    sale_dollars=row['sale_dollars'],
                    volume_sold_liters=row['volume_sold_liters'],
                    volume_sold_gallons=row['volume_sold_gallons']
                )
                product.save()
        self.stdout.write(self.style.SUCCESS('Products imported successfully!'))

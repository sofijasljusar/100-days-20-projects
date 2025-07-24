import csv
from django.core.management.base import BaseCommand
from cafes.models import Cafe


class Command(BaseCommand):
    help = "Import cafes from CSV file"

    def add_arguments(self, parser):
        parser.add_argument('csv_filepath', type=str, help='Path to the cafes CSV file')

    def handle(self, *args, **kwargs):
        filepath = kwargs['csv_filepath']
        with open(filepath, newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            count = 0
            for i, row in enumerate(reader):
                print(f"Processing row {i}: {row['name']}")
                # Convert string "True"/"False" to boolean for boolean fields
                has_sockets = row['has_sockets'].lower() in ('true', '1', 'yes')
                has_toilet = row['has_toilet'].lower() in ('true', '1', 'yes')
                has_wifi = row['has_wifi'].lower() in ('true', '1', 'yes')
                can_take_calls = row['can_take_calls'].lower() in ('true', '1', 'yes')

                cafe, created = Cafe.objects.update_or_create(
                    name=row['name'],
                    defaults={
                        'map_url': row['map_url'],
                        'img_url': row['img_url'],
                        'location': row['location'],
                        'has_sockets': has_sockets,
                        'has_toilet': has_toilet,
                        'has_wifi': has_wifi,
                        'can_take_calls': can_take_calls,
                        'seats': row.get('seats', '') or None,
                        'coffee_price': row.get('coffee_price', '') or None,
                    }
                )
                count += 1

            self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} cafes.'))

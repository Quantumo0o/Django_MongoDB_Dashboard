import os
import json
from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from django.utils.timezone import make_aware
from datetime import datetime
from myapp.models import Insight  # Adjust this import according to your app name

class Command(BaseCommand):
    help = 'Load data from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **options):
        json_file_path = options['json_file']
        if not os.path.exists(json_file_path):
            self.stdout.write(self.style.ERROR(f"File not found: {json_file_path}"))
            return

        try:
            with open(json_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except json.JSONDecodeError as e:
            self.stdout.write(self.style.ERROR(f"Error parsing JSON file: {e}"))
            return

        '''required_fields_defaults = {
            'sector': 'Unknown Sector',
            'topic': 'General',
            'region': 'Unknown Region',
            'country': 'Unknown Country',
            'pestle': 'General',
            'title': 'Untitled Insight'
        }'''

        skipped_items = []
        saved_items = []

        for item in data:
            # Validate item structure
            if not isinstance(item, dict):
                skipped_items.append(item)
                self.stdout.write(self.style.WARNING(f"Invalid item structure: {item}"))
                continue

            # Parse and validate dates
            added_date = self.parse_date(item.get('added'))
            published_date = self.parse_date(item.get('published'))

            # Ensure all required fields are not blank
            '''for field, default in required_fields_defaults.items():
                if not item.get(field):
                    self.stdout.write(self.style.WARNING(f"Field {field} is missing. Using default value: {default}."))
                    item[field] = default'''

            # Validate field length constraints
            '''if len(item.get('title', '')) > 255:
                self.stdout.write(self.style.WARNING(f"Title too long: {item['title']}. Truncating to 255 characters."))
                item['title'] = item['title'][:255]
            if len(item.get('url', '')) > 200:
                self.stdout.write(self.style.WARNING(f"URL too long: {item['url']}. Truncating to 200 characters."))
                item['url'] = item['url'][:200]'''

            # Validate integer fields
            ''' try:
                    intensity = int(item.get('intensity', 0) or 0)
                    likelihood = int(item.get('likelihood', 0) or 0)
                except ValueError:
                    self.stdout.write(self.style.WARNING("Invalid integer values for intensity or likelihood. Using default value 0."))
                    intensity = 0
                    likelihood = 0'''

            # Create and save the Insight object
            insight = Insight(
                end_year=item.get('end_year', ''),
                intensity=None if item.get('intensity') == '' else int(item.get('intensity', 0)),
                sector=item['sector'],
                topic=item['topic'],
                insight=item['insight'],
                url=item['url'],
                region=item['region'],
                start_year=item.get('start_year', ''),
                impact=item.get('impact', ''),
                added=added_date,
                published=published_date,
                country=item['country'],
                relevance=None if item.get('relevance') == '' else int(item.get('relevance', 0)),
                pestle=item['pestle'],
                source=item['source'],
                title=item['title'],
                likelihood=None if item.get('likelihood') == '' else int(item.get('likelihood', 0)),
            )
            try:
                insight.full_clean()  # Validate the model instance
                insight.save()
                saved_items.append(insight.title)
                self.stdout.write(self.style.SUCCESS(f"Successfully saved insight: {insight.title}"))
            except ValidationError as e:
                self.stdout.write(self.style.ERROR(f"Error saving insight: {e}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Unexpected error: {e}"))

        if skipped_items:
            self.stdout.write(self.style.WARNING(f"Skipped {len(skipped_items)} items due to invalid structure or missing fields."))
        if saved_items:
            self.stdout.write(self.style.SUCCESS(f"Successfully saved {len(saved_items)} insights."))

    def parse_date(self, date_str):
        try:
            naive_datetime = datetime.strptime(date_str, '%B, %d %Y %H:%M:%S')
            return make_aware(naive_datetime)
        except (ValueError, TypeError):
            return None

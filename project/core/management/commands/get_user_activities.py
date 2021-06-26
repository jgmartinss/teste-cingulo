import json
import requests

from datetime import datetime, timedelta

from django.db import transaction, IntegrityError
from django.core.management.base import BaseCommand

from project.core.models import UserActivities


class Command(BaseCommand):
    help = "Get user activities"

    def add_arguments(self, parser):
        parser.add_argument('--ref_year', type=int)

    def handle(self, *args, **options):
        self.print_log('Start - Get user activities...', 'S')

        base_url = 'https://static.cingulo.com/bi/user_activities.json'
        req = requests.get(base_url)

        if req.status_code != 200:
            self.print_log('Faill', 'W')
            return

        data = json.loads(req.content)
        ref_year = options.get('ref_year')

        if not ref_year:
            self.print_log('Error: --ref_year is required', 'W')
            return

        objs = []

        for row in data:
            i = 0
            data = {}

            for each_row in row['activities']:
                i = i + 1
                data.update({self.day_of_year_to_date(ref_year, i): each_row})

            _obj = UserActivities(
                **{
                    'id_user': row['id'],
                    'ref_year': ref_year,
                    'data': data,
                }
            )
            objs.append(_obj)

        with transaction.atomic():
            try:
                UserActivities.objects.bulk_create(objs)
            except IntegrityError as e:
                self.print_log(f'Error: {e}', 'S')
                return

        self.print_log(f'Inserted {len(objs)} total records...', 'S')
        self.print_log('Done!', 'S')

    def day_of_year_to_date(self, year, day):
        date = datetime(year, 1, 1) + timedelta(day - 1)
        return str(date.date())

    def print_log(self, msg, _type):
        self.stdout.write(
            self.style.SUCCESS(msg) if _type == 'S' else self.style.WARNING(msg)
        )

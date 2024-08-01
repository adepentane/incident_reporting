
from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Clears migration history for the specified app'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM django_migrations WHERE app = 'reports';")
        self.stdout.write(self.style.SUCCESS('Successfully cleared migration history for reports app'))
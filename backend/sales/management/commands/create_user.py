# backend/app/management/commands/create_user.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a simple user'

    def handle(self, *args, **kwargs):
        username = 'simpleuser'
        password = 'password123'  # Use a secure password in production
        email = 'simpleuser@example.com'  # Optional

        # Check if the user already exists
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, password=password, email=email)
            self.stdout.write(self.style.SUCCESS(f'User {username} created successfully!'))
        else:
            self.stdout.write(self.style.WARNING(f'User {username} already exists.'))

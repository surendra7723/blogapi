from django.core.management.base import BaseCommand
from accounts.models import CustomUser
from faker import Faker

class Command(BaseCommand):
    help = 'Populate the database with 50 fake users.'

    def handle(self, *args, **kwargs):
        fake = Faker()
        users = []
        for _ in range(50):
            username = fake.unique.user_name()
            email = fake.unique.email()
            name = fake.name()
            password = 'password123'  # default password for all
            user = CustomUser(
                username=username,
                email=email,
                name=name,
                is_active=True
            )
            user.set_password(password)
            users.append(user)
        CustomUser.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS('Successfully created 50 users.'))

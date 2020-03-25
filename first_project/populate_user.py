import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from first_app.models import User
from faker import Faker

fakegen = Faker()

def populate(n=5):
    for entry in range(n):
        f_name = fakegen.first_name()
        l_name = fakegen.last_name()
        email = fakegen.email()

        user = User.objects.get_or_create(f_name=f_name, l_name=l_name, email=email)[0]

if __name__ == '__main__':
    print("populating user script")
    populate(20)
    print("populating complete!")
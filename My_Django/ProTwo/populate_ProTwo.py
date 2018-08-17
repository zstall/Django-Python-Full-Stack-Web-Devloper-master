import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

# Fake Population script
import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def add_users(N=5):
    for entry in range(N):
        n = fakegen.name()
        f_name = n.split()[0]
        l_name = n.split()[1]
        u_email = fakegen.email()
        print(f_name + " " + l_name + " " + str(u_email))

        user_info = User.objects.get_or_create(first_name=f_name, last_name=l_name, email=u_email)[0]

if __name__ == '__main__':
    print("Loading data...")
    add_users(2)
    print("Users Loaded")

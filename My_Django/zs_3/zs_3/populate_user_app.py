import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','zs_3.settings')

import django
django.setup()

# Fake pop script
import random
from user_app.models import User,Username,Email
from faker import Faker

fakegen = Faker()



def add_username():
    nl = fakegen.name()
    p = Username.objects.get_or_create(user_name=nl)[0]
    p.save()
    return p

def populate(N=5):

    for entry in range(N):

        # Add fake data for that entry
        name_login = add_username()

        first_name = name_login.user_name.split()[0]
        last_name = name_login.user_name.split()[1]
        user_email = fakegen.email()

        # Create the user first and last name entry
        user_info = User.objects.get_or_create(u_name=name_login, f_name=first_name, l_name=last_name)[0]

        # create a email address entry
        e = Email.objects.get_or_create(person=user_info, u_email=user_email)[0]



if __name__ == '__main__':
    print("populate script!")
    populate(20)
    print("populating complete!")

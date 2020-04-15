import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()


import random
from first_app.models import AccessRecord,computer_science,electronics
from faker import Faker

fakegen=Faker()
topics=['search','social','Marketplace','News','Games']

def add_topic():
    t=Topic.objects.get_or_create(top-name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

        top=add_topic()
        fake_url = fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake-name)[0]

        acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_dat)[0]

if __name__=='__main__':
    print("population")
    populate(20)
    print("completed")

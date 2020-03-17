import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','RadioChannel.settings')

import django
django.setup()


import random
from stream.models import Podcast
from faker import Faker

fakegen = Faker()

def add_show(N=20):
    for _ in range(N):
        fake_url= fakegen.url()
        fake_name = fakegen.name()
        fake_title = fakegen.sentence()

        show = Podcast.objects.get_or_create(url=fake_url, title=fake_title, rj_name=fake_name)[0]


if __name__ == '__main__':
    print('Populating...')
    add_show()
    print('Done!')

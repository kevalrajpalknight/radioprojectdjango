# Generated by Django 2.2.7 on 2020-03-15 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0002_liveshow'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='description',
            field=models.TextField(blank=True, max_length=1024),
        ),
    ]

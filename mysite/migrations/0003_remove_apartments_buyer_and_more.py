# Generated by Django 4.1.2 on 2022-10-20 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_alter_apartments_buyer_alter_apartments_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartments',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='apartmentsell',
            name='owner_sell',
        ),
    ]

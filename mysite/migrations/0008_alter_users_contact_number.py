# Generated by Django 4.1.2 on 2022-10-20 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_remove_apartments_owner_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='contact_number',
            field=models.CharField(max_length=30, verbose_name='Телефооон'),
        ),
    ]

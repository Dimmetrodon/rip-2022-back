# Generated by Django 4.1.2 on 2022-10-20 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_remove_apartments_buyer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentsell',
            name='buyer_sell',
            field=models.ForeignKey(db_column='buyer_sell', on_delete=django.db.models.deletion.DO_NOTHING, related_name='buyer_sell', to='mysite.users', verbose_name='Владелец'),
        ),
    ]

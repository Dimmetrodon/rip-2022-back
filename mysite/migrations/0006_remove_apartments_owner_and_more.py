# Generated by Django 4.1.2 on 2022-10-20 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_remove_apartmentsell_buyer_sell_apartmentsell_buyer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartments',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='apartmentsell',
            name='apartment',
        ),
        migrations.RemoveField(
            model_name='apartmentsell',
            name='buyer',
        ),
        migrations.AddField(
            model_name='apartments',
            name='owner_id',
            field=models.ForeignKey(blank=True, db_column='owner_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='owner_id', to='mysite.users', verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='apartmentsell',
            name='apartment_id',
            field=models.ForeignKey(blank=True, db_column='apartment_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mysite.apartments', verbose_name='Квартира'),
        ),
        migrations.AddField(
            model_name='apartmentsell',
            name='buyer_id',
            field=models.ForeignKey(blank=True, db_column='buyer_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='buyer_id', to='mysite.users', verbose_name='Владелец'),
        ),
    ]

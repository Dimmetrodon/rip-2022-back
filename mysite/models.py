from django.db import models


class Apartments(models.Model):
    name = models.CharField(max_length=30, verbose_name="Квартира")
    description = models.CharField(max_length=255, verbose_name="Описание")
    owner = models.ForeignKey('Users', models.DO_NOTHING, db_column='owner_id', verbose_name="Владелец", blank=True, null=True,  related_name='owner')
    cost = models.IntegerField(blank=True, null=True)

class Users(models.Model):
    user_name = models.CharField(max_length=30, verbose_name="Имя")
    contact_number = models.CharField(max_length=30, verbose_name="Телефон")


class ApartmentSell(models.Model):
    post_date = models.CharField(max_length=30, verbose_name="Дата выставки на продажу")
    status = models.CharField(max_length=30, verbose_name="Статус")
    apartment = models.ForeignKey('Apartments', models.DO_NOTHING, db_column='apartment', blank=True, null=True, verbose_name="Квартира")
    buyer = models.ForeignKey('Users', models.DO_NOTHING, db_column='buyer', verbose_name="Владелец" ,blank=True, null=True, related_name='buyer')

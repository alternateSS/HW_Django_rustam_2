from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название товара')
    price = models.IntegerField(verbose_name='Цена товара')

    def __str__(self):
        return self.name


class Purchase(models.Model):
    name = models.CharField(max_length=30, verbose_name='ФИО покупателя')
    age = models.IntegerField(verbose_name='Возраст клиента')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='purch')
    date_purchase = models.DateField(auto_now_add=True, verbose_name='Дата покупки')
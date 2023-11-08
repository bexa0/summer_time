from django.db import models


class Parent(models.Model):
    name = models.CharField('Name', max_length=50)
    surname = models.CharField('Surname', max_length=50)
    age = models.PositiveIntegerField('Age')

    def __str__(self):
        return f'{self.name} - {self.surname}'


class Child(models.Model):
    name = models.CharField('Name', max_length=50)
    surname = models.CharField('Surname', max_length=50)
    age = models.PositiveIntegerField('Age')
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, verbose_name='Parent')

    def __str__(self):
        return f'{self.name} - {self.parent.surname}'


class Icecream(models.Model):
    name = models.CharField('Icecream', max_length=100)

    def __str__(self):
        return self.name


class Shop(models.Model):
    label = models.CharField('Label', max_length=100)
    icecream = models.ManyToManyField('Icecream')

    def __str__(self):
        return f'{self.label}'


class ShopSale(models.Model):
    date = models.DateField('Date')
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    icecream_sale = models.ForeignKey(Icecream, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.child} - {self.icecream_sale}'

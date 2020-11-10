from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Division(models.Model):
    name = models.CharField(max_length=128, verbose_name='Наименование')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)


class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    desc = models.CharField(max_length=220, verbose_name='Описание')
    fot = models.IntegerField(verbose_name='Фонд оплаты труда')

class Priority(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    desc = models.CharField(max_length=220, verbose_name='Описание')

class State(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    desc = models.CharField(max_length=220, verbose_name='Описание')

    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    volume = models.IntegerField(verbose_name='Объем работ')
    deadline = models.DateTimeField(verbose_name='Выполнить до', blank=True, null=True)
    money = models.IntegerField(verbose_name='Деньги', blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name='Наименование')
    desc = models.CharField(max_length=200, verbose_name='Содержание', blank=True, null=True)
    notes = models.CharField(max_length=200, verbose_name='Примечание', blank=True, null=True)
    responsible = models.ForeignKey(Profile, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    prevTask = models.ForeignKey('self', blank=True, null=True, related_name='task', on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

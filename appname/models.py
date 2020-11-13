from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
ACTION = [('+', 'Приход'),('-', 'Расход')]
TYPE_TASK = [(1,'Продажи'),(2,'Работа')]


class Division(models.Model):
    name = models.CharField(max_length=128, verbose_name='Наименование')

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    telephone = models.CharField(verbose_name='Контактный теллефон', max_length=12)


class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    desc = models.CharField(max_length=220, verbose_name='Описание')
    fot = models.IntegerField(verbose_name='Фонд оплаты труда')
    date = models.DateField(verbose_name='Дата создания', blank=True, null=True, default=datetime.now())
    file = models.FileField(verbose_name='Файл', upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.name


class Priority(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    desc = models.CharField(max_length=220, verbose_name='Описание')

    def __str__(self):
        return self.name


class State(models.Model):                                                     #статус задачи
    name = models.CharField(max_length=100, verbose_name='Наименование')
    desc = models.CharField(max_length=220, verbose_name='Описание')

    def __str__(self):
        return self.name


class Task(models.Model):
    type = models.IntegerField(choices=TYPE_TASK, default=2)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name='Дата начала')
    plan_days = models.IntegerField(verbose_name='Плановое кол-во дней')
    cost_of_advance = models.BigIntegerField(verbose_name='Стоимость опережения за один день')
    cost_of_delay = models.BigIntegerField(verbose_name='Стоимость задержки за один день')
    min_days = models.IntegerField(verbose_name='Минимальное кол-во дней')
    data_fact_end = models.DateField(verbose_name='Фактическое время выполнения', blank=True, null=True)
    cost_for_min_days = models.BigIntegerField(verbose_name='Стоимость уменьшения до мин кол-ва дней')
    name = models.CharField(max_length=100, verbose_name='Наименование')
    desc = models.CharField(max_length=200, verbose_name='Содержание', blank=True, null=True)
    notes = models.CharField(max_length=200, verbose_name='Примечание', blank=True, null=True)
    responsible = models.ForeignKey(Profile, on_delete=models.CASCADE)
    prev_task = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    master = models.ForeignKey('MasterTask', blank=True, null=True, on_delete=models.SET_NULL, related_name='master')


    def __str__(self):
        return self.name

class MasterTask(models.Model):
    task = models.ForeignKey(Task, verbose_name='Подчиненный процесс', on_delete=models.SET_NULL, blank=True, null=True)


class Resource(models.Model):
    name = models.CharField(max_length=20, verbose_name='Материалы')
    measure_unit = models.CharField(max_length=20, verbose_name='Единицы измерения')

    def __str__(self):
        return self.name


class Journal(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Задача')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, verbose_name='Ресурс')
    type = models.CharField(max_length=1, choices=ACTION, verbose_name='Тип операции')
    quantity = models.IntegerField(verbose_name='Кол-во')
    date = models.DateTimeField(verbose_name='Дата проведения')

    def __str__(self):
        return self.resource.name + ' ' + self.type + ' ' + self.date.strftime("%Y-%m-%d-%H.%M.%S")

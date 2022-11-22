from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator


'''
class Registration(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    lastname=models.CharField(max_length=150, verbose_name='Фамилия')
    email = models.EmailField(max_length=100, verbose_name='email')
    password = models.CharField(max_length=150, verbose_name='Пароль')
    #theme = models.CharField(max_length=150, verbose_name='Тема выступления')
    #time = models.CharField(max_length=150, verbose_name='Время выступления')


    def get_absolute_url(self):
        return reverse('view_registration', kwargs={"registration_id": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name ='Регистрация'
        verbose_name_plural ='Регистрация'

#class RegSpiker(models.Model):
 #   photo=models.ImageField(upload_to='photos/%Y/%m/%d/')


'''
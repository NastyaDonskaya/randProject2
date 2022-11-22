# Generated by Django 3.2.8 on 2022-11-21 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20211013_2327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=100, verbose_name='email')),
                ('password', models.CharField(max_length=150, verbose_name='Пароль')),
            ],
            options={
                'verbose_name': 'Регистрация',
                'verbose_name_plural': 'Регистрация',
            },
        ),
        migrations.DeleteModel(
            name='AddReport',
        ),
        migrations.DeleteModel(
            name='RegistrationGuest',
        ),
        migrations.DeleteModel(
            name='RegistrationSpiker',
        ),
    ]

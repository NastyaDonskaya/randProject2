# Generated by Django 3.2.8 on 2021-10-13 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationguest',
            old_name='surname',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='registrationspiker',
            old_name='surname',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='registrationspiker',
            old_name='phoneNumber',
            new_name='phone',
        ),
        migrations.AlterField(
            model_name='addreport',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='registrationguest',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='registrationspiker',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

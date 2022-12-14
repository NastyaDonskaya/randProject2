# Generated by Django 3.2.8 on 2022-11-24 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_numbers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='numbers',
            old_name='randNum',
            new_name='rand_num',
        ),
        migrations.RenameField(
            model_name='numbers',
            old_name='userName',
            new_name='user_name',
        ),
        migrations.AddField(
            model_name='numbers',
            name='count_num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='numbers',
            name='left_num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='numbers',
            name='right_num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-21 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]

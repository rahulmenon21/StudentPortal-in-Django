# Generated by Django 4.1.4 on 2022-12-19 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'verbose_name': 'notes', 'verbose_name_plural': 'notes'},
        ),
        migrations.AlterModelTable(
            name='notes',
            table=None,
        ),
    ]
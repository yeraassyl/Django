# Generated by Django 3.0.5 on 2020-04-17 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200417_1316'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name': 'ToDo task', 'verbose_name_plural': 'ToDo tasks'},
        ),
    ]
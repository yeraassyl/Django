# Generated by Django 3.0.5 on 2020-04-17 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todolist',
            options={'verbose_name': 'ToDo', 'verbose_name_plural': 'ToDo lists'},
        ),
    ]